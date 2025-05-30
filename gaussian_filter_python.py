import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

x = np.arange(1, 101)
A = np.cos(2 * np.pi * 0.05 * x + 2 * np.pi * np.random.rand()) + 0.5 * np.random.randn(100)
B = gaussian_filter1d(A, sigma=1)     # ~ small window
C = gaussian_filter1d(A, sigma=5)     # larger window (smoother)

# Plotting
plt.plot(x, A, '--', label='A - Initial with noise')
plt.plot(x, B, '-o', label='B - Small Window (σ=1)')
plt.plot(x, C, '-x', label='C - Large Window (σ=5)')
plt.legend()
plt.title('Gaussian Filter Smoothing in Python')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()
