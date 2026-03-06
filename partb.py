import numpy as np
import matplotlib.pyplot as plt

# Load initial positions (snapshot 0)
file_path_initial = r'C:\Users\LC15\Desktop\Stat Mech\Active_BrownianParticle_DataSet\Active_BrownianParticle_DataSet\Finalized_data\DataSet2\part\NOISE_tra0'
with open(file_path_initial, 'rb') as myinitialFile:
    initial_data = np.fromfile(myinitialFile, dtype=np.float64)

N = 3517
x_position_i = initial_data[0:N]
y_position_i = initial_data[N:2*N+1]

times = []
MSD_values = []

# Loop through snapshots from 10 to 10000 in steps of 10
for i in range(10, 10001, 10):
    file_path = rf'C:\Users\LC15\Desktop\Stat Mech\Active_BrownianParticle_DataSet\Active_BrownianParticle_DataSet\Finalized_data\DataSet2\part\NOISE_tra{i}'
    with open(file_path, 'rb') as f:
        data = np.fromfile(f, dtype=np.float64)
    
    x_position_f = data[0:N]
    y_position_f = data[N:2*N]
    
    # Calculate displacement differences
    x_diff = x_position_f - x_position_i
    y_diff = y_position_f - y_position_i
    
    # Calculate squared displacement and mean over all particles
    diff_sq_sum = np.square(x_diff) + np.square(y_diff)
    MSD = np.mean(diff_sq_sum)
    
    time_diff = i * 0.001  # 0.001s between snapshots times snapshot index
    times.append(time_diff)
    MSD_values.append(MSD)


# Plot graph of MSD vs time
plt.loglog(np.log(times), np.log(MSD_values), label='MSD vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Mean Square Displacement')
plt.title('MSD vs Time for Brownian Particles')
plt.legend()
plt.grid(True)
plt.show()




# for dataset4

# import numpy as np
# import matplotlib.pyplot as plt

# # Load initial positions (snapshot 0)
# file_path_initial = r'C:\Users\LC15\Desktop\Stat Mech\Active_BrownianParticle_DataSet\Active_BrownianParticle_DataSet\Finalized_data\DataSet4\part\POSITION0'
# with open(file_path_initial, 'rb') as myinitialFile:
#     initial_data = np.fromfile(myinitialFile, dtype=np.float64)

# N = 3000
# x_position_i = initial_data[0:N]
# y_position_i = initial_data[N:2*N]

# times = []
# MSD_values = []

# # Loop through snapshots from 10 to 10000 in steps of 10
# for i in range(10, 1000001, 10):
#     file_path = rf'C:\Users\LC15\Desktop\Stat Mech\Active_BrownianParticle_DataSet\Active_BrownianParticle_DataSet\Finalized_data\DataSet4\part\POSITION{i}'
#     with open(file_path, 'rb') as f:
#         data = np.fromfile(f, dtype=np.float64)
    
#     x_position_f = data[0:N]
#     y_position_f = data[N:2*N]
    
#     # Calculate displacement differences
#     x_diff = x_position_f - x_position_i
#     y_diff = y_position_f - y_position_i
    
#     # Calculate squared displacement and mean over all particles
#     diff_sq_sum = np.square(x_diff) + np.square(y_diff)
#     MSD = np.mean(diff_sq_sum)
    
#     time_diff = i * 0.001  # 0.001s between snapshots times snapshot index
#     times.append(time_diff)
#     MSD_values.append(MSD)


# # Plot graph of MSD vs time
# plt.loglog(times, MSD_values, label='MSD vs Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Mean Square Displacement')
# plt.title('MSD vs Time for Brownian Particles')
# plt.legend()
# plt.grid(True)
# plt.show()

