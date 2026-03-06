# for the initial and final position
import numpy as np
import matplotlib.pyplot as plt


file_path = r'C:\Users\LC15\Desktop\Stat Mech\Active_BrownianParticle_DataSet\Active_BrownianParticle_DataSet\Finalized_data\DataSet1\part\POSITION10000'
with open(file_path, 'rb') as myFile:
    data = np.fromfile(myFile, dtype=np.float64)


x_position = data[0:3517]
y_position = data[3517:7035]


print(data)
print(len(data))
plt.plot(x_position, y_position ,marker='o', markersize=4)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Active Brownian Particle Positions \n DataSet1 initial')
plt.show()






# initial and final position in one graph

import numpy as np
import matplotlib.pyplot as plt


for i in [0, 10000]:
    file_path = rf'C:\Users\LC15\Desktop\Stat Mech\Active_BrownianParticle_DataSet\Active_BrownianParticle_DataSet\Finalized_data\DataSet2\part\NOISE_tra{i}'
    data = np.fromfile(file_path, dtype=np.float64)
    x_position = data[0:3517]
    y_position = data[3517:7035] 
    plt.scatter(x_position, y_position, label=f'POSITION{i}')
   

plt.legend()
plt.show()








