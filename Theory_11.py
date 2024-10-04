# Code for Discrete Wavelength Transform
import pywt
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal
t = np.linspace(0, 1, num=1024)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)

# Perform Discrete Wavelet Transform (DWT) using the 'db4' wavelet
wavelet = 'db4'
coeffs = pywt.wavedec(signal, wavelet)

# Coefficients consist of (cA_n, cD_n, cD_n-1, ..., cD_1)
# cA_n is the approximation coefficients
# cD_n, ..., cD_1 are the detail coefficients at different levels
cA, *cD = coeffs

# Plot the original signal
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')

# Plot the approximation coefficients (cA) and detail coefficients (cD)
plt.subplot(2, 1, 2)
plt.plot(cA)
plt.title('Approximation Coefficients (cA)')
plt.tight_layout()

plt.show()

# You can also access the detail coefficients and plot them as needed
for i, detail_coeff in enumerate(cD, start=1):
    plt.figure(figsize=(10, 3))
    plt.plot(detail_coeff)
    plt.title(f'Detail Coefficients (cD_{i})')
    plt.show()
