import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import cv2

def calibrate_plot(rvecs, tvecs, chess_pts_list, fig):
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

def drawAxis(img, origin, imgpts):
    img = cv2.line(img, origin, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, origin, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, origin, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

def render_axes(img, K, dist_coeffs, chess_pts_list, corners):
    # Undistort
    undistort_frame = cv2.undistort(img, K, dist_coeffs)
    
    # Find world pose of chessboard pattern
    chess_pts = chess_pts_list[len(chess_pts_list) - 1]
    _, rvec, tvec = cv2.solvePnP(chess_pts, corners, K, dist_coeffs)

    # Project axises
    three_axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3) * 50
    imgpts, jac = cv2.projectPoints(three_axis, rvec, tvec, K, dist_coeffs) 
    origin = tuple(corners[0].ravel())
    axis_frame = drawAxis(undistort_frame, origin, imgpts)
    return axis_frame