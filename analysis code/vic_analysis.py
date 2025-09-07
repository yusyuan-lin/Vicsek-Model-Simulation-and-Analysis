import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from nolds import dfa, hurst_rs, sampen


# Load data
data = np.loadtxt('vicsek_data.txt')

# Extract positions and velocities
positions = data[:, :2]
velocities = data[:, 2:]

# Parameters
L = 10
N = 100
v0 = 0.1
eta = 1.0
dt = 0.01
timesteps = 10000


# Compute speed and direction
speeds = np.linalg.norm(velocities, axis=1)
directions = np.arctan2(velocities[:, 1], velocities[:, 0])

# Scale speeds to range [0, 1]
speeds /= np.max(speeds)

# Compute probability density function of speeds
pdf, edges = np.histogram(speeds, bins=50, range=(0, 1), density=True)
bin_centers = (edges[:-1] + edges[1:]) / 2

# Compute detrended fluctuation analysis
if len(speeds) > 100:
    alpha = dfa(np.log(speeds), overlap=True)
    hurst = hurst_rs(speeds)
else:
    alpha = np.nan
    hurst = np.nan

# calculate multi-scale entropy
mse = sampen(data, emb_dim=2, tolerance=0.15)

# Compute correlation analysis
corr = np.corrcoef(speeds[:-1], speeds[1:])[0, 1]

# Print multiscale entropy and correlation coefficient
print(f'Multiscale entropy: {mse:.2f}')
print(f'Correlation coefficient: {corr:.2f}')

# Plot results
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].scatter(positions[:, 0], positions[:, 1], s=1)
axs[0, 0].set(xlim=(-L/2, L/2), ylim=(-L/2, L/2), xlabel='x', ylabel='y', aspect='equal')
axs[0, 1].plot(bin_centers, pdf)
axs[0, 1].set(xlabel='Speed', ylabel='Probability density')
axs[1, 0].plot(np.log10(range(1, len(speeds))), np.log10(np.sqrt(np.cumsum(np.ediff1d(speeds)**2))))
axs[1, 0].plot(np.log10(range(1, len(speeds))), alpha*np.log10(range(1, len(speeds))) + np.log10(0.5), 'r--')
axs[1, 0].set(xlabel='log(s)', ylabel='log(F(s))', title=f'DFA exponent: {alpha:.2f}', ylim=(-2, 2))
axs[1, 1].plot(np.log10(range(1, len(speeds))), hurst*np.log10(range(1, len(speeds))) + np.log10(0.5), 'r--')
axs[1, 1].set(xlabel='log(s)', ylabel='log(R/S)', title=f'Hurst exponent: {hurst:.2f}', ylim=(-2, 2))
plt.tight_layout()
plt.show()

