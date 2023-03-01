import matplotlib.pyplot as plt
import numpy as np

def visualize3D(arr, pair):
    
    x = arr[:, 0]
    y = arr[:, 1]
    z = arr[:, 2]
    
    fig = plt.figure(figsize=(8,8))
    fig.suptitle('Closest Point in 3D plot')
    ax = plt.axes(projection="3d")
    
    fg = ax.scatter3D(x, y, z, alpha = 0.5)
    fg = ax.scatter3D(pair[0][0], pair[0][1], pair[0][2], color='r', alpha = 1)
    fg = ax.scatter3D(pair[1][0], pair[1][1], pair[1][2], color='r', alpha = 1)
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    
    plt.show()
