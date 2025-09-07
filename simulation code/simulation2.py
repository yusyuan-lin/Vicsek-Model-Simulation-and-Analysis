import numpy as np

# Parameters
L = 10
N = 100
v0 = 0.1
eta = 1.0
dt = 0.01
timesteps = 10000

# Initialization
positions = np.random.rand(N, 2) * L
velocities = np.random.randn(N, 2)
velocities /= np.linalg.norm(velocities, axis=1)[:, np.newaxis]
velocities *= v0

# Simulation
for i in range(timesteps):
    # Update positions
    positions += velocities * dt

    # Apply periodic boundary conditions
    positions = np.mod(positions, L)

    # Compute average velocity direction
    theta = np.arctan2(velocities[:, 1], velocities[:, 0])
    theta_avg = np.zeros(N)
    for j in range(N):
        neighbors = np.sqrt(np.sum((positions - positions[j])**2, axis=1)) < 1.0
        theta_avg[j] = np.mean(theta[neighbors])

    # Update velocities
    velocities[:, 0] = v0 * np.cos(theta_avg) + eta * np.random.randn(N)
    velocities[:, 1] = v0 * np.sin(theta_avg) + eta * np.random.randn(N)
    velocities /= np.linalg.norm(velocities, axis=1)[:, np.newaxis]

# Save data to text file
np.savetxt('vicsek_data.txt', np.hstack([positions, velocities]), header='x y vx vy')
