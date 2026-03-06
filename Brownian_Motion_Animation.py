import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation

# ----- USER CONFIGURABLE -----
data_folder = r'C:\Users\LC15\Desktop\Stat Mech\Active_BrownianParticle_DataSet\Active_BrownianParticle_DataSet\Finalized_data\DataSet2\part'
num_particles = 3517
file_type = np.float64  # Change to np.float32 if your files use 4-byte floats
# ----------------------------

# Get all POSITION* files, sorted by index
position_files = sorted([
    f for f in os.listdir(data_folder) if f.startswith('POSITION')
], key=lambda f: int(f.replace('POSITION', '')))

fig, ax = plt.subplots(figsize=(7,7))
scat = ax.scatter([], [], s=3, alpha=0.6)
ax.set_xlim(-100, 100)  # Adjust as per your data range
ax.set_ylim(-100, 100)
ax.set_title('Brownian Particle Animation')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)

# Function to load and reshape one frame
def get_positions(idx):
    file_path = os.path.join(data_folder, position_files[idx])
    data = np.fromfile(file_path, dtype=file_type)
    return data.reshape(num_particles, 2)

# Update function for animation
def update(frame):
    positions = get_positions(frame)
    scat.set_offsets(positions[:, :2])
    ax.set_title(f'Brownian Particle Animation\nStep {frame} (File: {position_files[frame]})')
    return scat,

ani = FuncAnimation(fig, update, frames=len(position_files), interval=50, blit=True)
plt.show()
