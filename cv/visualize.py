import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def calibrate(rvecs, tvecs, chess_pts_list, fig):
    rvec = rvecs[len(rvecs)-1]
    tvec = tvecs[len(tvecs)-1]
    chess_pts = chess_pts_list[len(chess_pts_list) - 1]
    # print(rvec)
    # print(tvec)
    

    chess_pts = np.array(chess_pts)

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(np.append(chess_pts[:,0], tvec[0][0]), np.append(chess_pts[:,1], tvec[1][0]), np.append(chess_pts[:,2], tvec[2][0]), c='r', marker='o')

    plt.draw()
    plt.pause(0.00001)
    plt.ion()
    plt.show()