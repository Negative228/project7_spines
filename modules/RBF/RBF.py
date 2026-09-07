import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

if torch.cuda.is_available():
    torch.cuda.empty_cache()

class WeightCalculator:
    def __init__(self, input_dim, input_w=None):
        self.nIn = input_dim
        self.nOut = 1
        if input_w is None:
            self.weights = (torch.rand(self.nIn, dtype=torch.float32)*0.1-0.05).to(device)
        else:
            self.weights = torch.tensor(input_w, dtype=torch.float32).to(device)
        
    def update(self, netSp, targetSp, teta, *args, **kwargs):
        pixel_nod_grid_flatten = netSp.permute([1, 2, 0]).flatten(0, 1)
        batched_dot = torch.func.vmap(torch.dot)
        y_pixel_AllNod_flatten = batched_dot(pixel_nod_grid_flatten, 
                                             self.weights.unsqueeze(0).repeat(len(pixel_nod_grid_flatten), 1))
        delta = targetSp.flatten() - y_pixel_AllNod_flatten
        self.weights += teta * torch.matmul(delta, pixel_nod_grid_flatten) / self.nIn

    def get_weights(self):
        return self.weights.cpu().numpy()
        
    def get_normalized_weights(self):
        w = self.weights
        normalized = w - torch.min(w)
        normalized = normalized / torch.max(normalized)
        return normalized.cpu().numpy()

def construct_phi(image, sigma=1, batch_size=None, NodeX1=None, NodeX2=None,
                                   pixel_pos=None, center_pos=None):
    
    X1, X2 = image.shape
    
    if center_pos is None:
        if NodeX1 is None:
            NodeX1 = X1 // 16
        if NodeX2 is None:
            NodeX2 = X2 // 16
        
        step_x = max(1, X1 // NodeX1)
        step_y = max(1, X2 // NodeX2)
        
        x_coords = torch.arange(0, X1, step_x, dtype=torch.float32, device=device)
        y_coords = torch.arange(0, X2, step_y, dtype=torch.float32, device=device)
        
        xx, yy = torch.meshgrid(x_coords, y_coords, indexing='ij')
        node_centers = torch.stack([xx.ravel(), yy.ravel()], dim=-1)
        
        del xx, yy, x_coords, y_coords
    else:
        node_centers = torch.tensor(center_pos, dtype=torch.float32, device=device)
    
    nIn = node_centers.shape[0]
    targetSp_tensor = torch.tensor(image, dtype=torch.float32, device=device)
    
    if batch_size is None:
        batch_size = nIn
    
    row_indices = torch.arange(X1, dtype=torch.float32, device=device)  # [X1]
    col_indices = torch.arange(X2, dtype=torch.float32, device=device)  # [X2]
    
    batched_netSp_sparse = []
    
    for i in range(0, nIn, batch_size):
        this_batch_size = min(batch_size, nIn - i)
        batch_centers = node_centers[i:i+this_batch_size]
        
        sparse_matrices = []
        
        for j in range(this_batch_size):
            cx, cy = batch_centers[j]
            
            row_diff = row_indices.unsqueeze(1) - cx  # [X1, 1]
            col_diff = col_indices.unsqueeze(0) - cy  # [1, X2]
            
            dist_sq = row_diff**2 + col_diff**2
            
            rbf_values = torch.exp(-dist_sq / (2 * sigma * sigma))
            
            sparse_rbf = rbf_values.to_sparse()
            sparse_matrices.append(sparse_rbf)
            
            del row_diff, col_diff, dist_sq, rbf_values
        
        batched_netSp_sparse.append(torch.stack(sparse_matrices))
        del sparse_matrices, batch_centers
        
        torch.cuda.empty_cache()
    
    del node_centers, row_indices, col_indices
    torch.cuda.empty_cache()
    
    return batched_netSp_sparse, targetSp_tensor

def train_weights(netSp_sparse, targetSp_tensor, nIterations, start_teta,  decay_rate=0.9, input_w=None): #end_teta,
    seq_weights = []
    iters = []
    count = 0
    if type(targetSp_tensor) != torch.Tensor:
        targetSp_tensor = torch.tensor(targetSp_tensor, dtype=torch.float32).to(device)

    for batch in netSp_sparse:
        batch_size = len(batch)
        teta = start_teta
        try:
            batch_input_w = input_w[count:count+batch_size]
        except:
            batch_input_w = None
        model = WeightCalculator(batch_size, input_w=batch_input_w)
        count += batch_size
        this_batch = batch.to_dense()
        #print('hello')
        for i in range(nIterations):
            #teta = teta if teta > end_teta else end_teta
            model.update(this_batch, targetSp_tensor, teta=teta)
            

            teta = start_teta * decay_rate**i if teta > 0.01 else 0.01
        #iters += [i+1]
        seq_weights += list(model.get_weights())
        del model
        torch.cuda.empty_cache()
    iter_mean = np.mean(iters)
    return seq_weights#, iter_mean


def convert_3d_2d(netSp_sparse):
    netSp_sp = torch.cat(netSp_sparse, dim=0).coalesce()
    D1, D2, D3 = netSp_sp.shape
    idx = netSp_sp.indices()
    v = netSp_sp.values()
    new_row_idx = idx[0] 
    new_col_idx = idx[1] + idx[2] * D2
    new_indices = torch.stack([new_row_idx, new_col_idx])
    
    sparse_2d = torch.sparse_coo_tensor(new_indices, v, (D1, D2 * D3))
    del netSp_sp, idx, v, new_row_idx, new_col_idx, new_indices
    torch.cuda.empty_cache()
    return sparse_2d


def construct_yRBF(seq_weights, netSp_sparse):
    yRBF = torch.mm(torch.tensor(seq_weights, dtype=torch.float32).to(device).unsqueeze(0), 
                    convert_3d_2d(netSp_sparse)).reshape((netSp_sparse[0].shape[1], netSp_sparse[0].shape[2])).T
    return yRBF

