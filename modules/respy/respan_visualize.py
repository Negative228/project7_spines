import os
import tifffile
import numpy as np
import pandas as pd
from pathlib import Path

from .respan_prepare import get_zstack

def patch_spines(image_dir:str, image_name:str, alpha=0.2, replace_original=None, ):

    if replace_original is None:
        original_stack = tifffile.imread(f'{image_dir}/{image_name}')
    else:
        if Path(replace_original).is_dir():
            original_stack = get_zstack(replace_original)
        else:
            original_stack = tifffile.imread(replace_original)

    image_name = Path(image_name).stem
    spines_df = pd.read_csv(f'{image_dir}/Tables/{image_name}_detected_spines.csv')
    check1 = len(spines_df)
    spines_df = spines_df[~((spines_df['x'] == 0.0) & (spines_df['y'] == 0.0) & (spines_df['z'] == 0.0))]
    check2 = len(spines_df)
    spines_df.sort_values('spine_id', inplace=True)

    biggest_dendrite_id = spines_df['dendrite_id'].value_counts().argmax() + 1
    biggest_dendrite_spine_count = spines_df['dendrite_id'].value_counts().max()
    
    
    if check1 != check2:
        print(f'deleted {check1-check2} entries')
    
    original_mip = original_stack.max(axis=0)
    if len(original_mip.shape) == 3:
        H_orig, W_orig, _ = original_mip.shape
    else:
        H_orig, W_orig = original_mip.shape
    print(f"Обрабатываю {image_dir}\\{image_name}.tif...")
    print(f"Оригинал: {original_stack.shape}, MIP: {original_mip.shape}")
    print(f"Найдено шипиков: {len(spines_df)}")
    
    mip_files = sorted(Path(f'{image_dir}/Spine_Arrays').glob(f'Spine_MIPs_{image_name}_b*.tif'))
    vols_files = sorted(Path(f'{image_dir}/Spine_Arrays').glob(f'Spine_vols_{image_name}_b*.tif'))
    
    
    all_mip_crops = []
    for f in mip_files:
        batch = tifffile.imread(str(f))  # форма: [batch, 4, X, Y]
        for i in range(batch.shape[0]):
            all_mip_crops.append(batch[i])
    
    print(f"Загружено MIP-кропов: {len(all_mip_crops)}")
    #assert len(all_mip_crops) == len(spines_df), "Число кропов не совпадает с CSV!"
    

    mask_channels = [np.zeros((H_orig, W_orig), dtype=np.float32) for _ in range(4)]

    
    for idx, crop in enumerate(all_mip_crops):
        # Координаты центра шипика из CSV
        try:
            if spines_df.iloc[idx]['dendrite_id'] != biggest_dendrite_id:
                continue
            x_center = int(round(spines_df.iloc[idx]['x']))
            y_center = int(round(spines_df.iloc[idx]['y']))
        except IndexError:
            break
        
        # Размер кропа
        try:
            _, crop_h, crop_w = crop.shape  # crop имеет форму [4, X, Y] (но не всегда)
        except ValueError:
            crop_h, crop_w = crop.shape
        
        # Координаты верхнего левого угла
        x0 = x_center - crop_w // 2
        y0 = y_center - crop_h // 2

        
        src_x0 = max(0, -x0)
        src_y0 = max(0, -y0)
        src_x1 = crop_w - max(0, x0 + crop_w - W_orig)
        src_y1 = crop_h - max(0, y0 + crop_h - H_orig)
        
        dst_x0 = max(0, x0)
        dst_y0 = max(0, y0)
        dst_x1 = dst_x0 + (src_x1 - src_x0)
        dst_y1 = dst_y0 + (src_y1 - src_y0)
        
        for c in range(4):
            # Используем np.maximum, чтобы при наложении overlapping кропов
            # сохранялось максимальное значение (а не перезаписывалось)
            try:
                mask_channels[c][dst_y0:dst_y1, dst_x0:dst_x1] = np.maximum(
                    mask_channels[c][dst_y0:dst_y1, dst_x0:dst_x1],
                    crop[c, src_y0:src_y1, src_x0:src_x1])
            except IndexError:
                mask_channels[c][dst_y0:dst_y1, dst_x0:dst_x1] = np.maximum(
                    mask_channels[c][dst_y0:dst_y1, dst_x0:dst_x1],
                    crop[src_y0:src_y1, src_x0:src_x1])

    
    color_overlay = np.stack([mask_channels[0], mask_channels[1], mask_channels[2], mask_channels[3]], axis=-1)
    orig_norm = original_mip.astype(np.float32) 
    orig_norm = (orig_norm - orig_norm.min()) / (orig_norm.max() - orig_norm.min() + 1e-8)
    if len(orig_norm.shape) == 2:
        orig_rgb = np.stack([orig_norm, orig_norm, orig_norm, np.ones(orig_norm.shape)], axis=-1)  # серый -> RGBA
    else:
        orig_rgb = np.concatenate([orig_norm, np.ones((*orig_norm.shape[:2], 1))], axis=-1)

    alpha = 0.2 
    combined = (1 - alpha) * orig_rgb + alpha * color_overlay
    combined = np.clip(combined, 0, 1)
    
    return combined, color_overlay, biggest_dendrite_spine_count