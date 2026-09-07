import numpy as np
import pywt

def anscombe_forward(x):
    return 2.0 * np.sqrt(np.maximum(x+3.0/8.0, 0.0))

def estimate_noise_wavelet(img, wavelet='db2'):
    coeffs = pywt.dwt2(img, wavelet)
    cH, cV, cD = coeffs[1]
    details = np.hstack([cH.ravel(), cV.ravel(), cD.ravel()])
    sigma = np.median(np.abs(details)) / 0.6745
    return sigma

def estimate_snr_wavelet(img, wavelet='db2', levels=3):
    img = np.asarray(img, dtype=np.float32)
    
    a_img = anscombe_forward(img)
    
    coeffs = pywt.wavedec2(a_img, wavelet, level=levels)
    
    cH, cV, cD = coeffs[-1]
    details = np.hstack([cH.ravel(), cV.ravel(), cD.ravel()])
    sigma = np.median(np.abs(details)) / 0.6745
    
    if sigma < 1e-9:
        return float('inf')  # Чистый сигнал без шума
    
    signal_coeffs = [coeffs[0]]  
    
    for i in range(1, len(coeffs) - 1):
        signal_coeffs.append(coeffs[i])
    
    signal_coeffs.append((
        np.zeros_like(coeffs[-1][0]),
        np.zeros_like(coeffs[-1][1]),
        np.zeros_like(coeffs[-1][2])
    ))
    
    signal_img = pywt.waverec2(signal_coeffs, wavelet)
    signal_img = signal_img[:a_img.shape[0], :a_img.shape[1]]
    
    signal_var = np.var(signal_img) #- sigma*sigma
    
    if signal_var < 1e-10:
        return float('-inf')  # Сигнала нет
    
    snr = 10.0 * np.log10(signal_var / (sigma ** 2))
    return snr

def estimate_snr(img):
    a_img = anscombe_forward(img)
    sigma = estimate_noise_wavelet(a_img)
    signal_var = np.var(a_img) - sigma * sigma
    snr = 10 * np.log10(max(signal_var, 1e-9)/sigma/sigma) #if sigma > 1e-9 else np.inf
    return snr