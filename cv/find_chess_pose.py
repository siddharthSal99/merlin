import cv2
import numpy as np

def find_chess_corners(img, chess_shape=(7, 9)):
    found, corners = cv2.findChessboardCorners(img, chess_shape)
    chess_img = cv2.drawChessboardCorners(img, chess_shape, corners, found)
    return (corners, chess_img)
    # cv2.imshow('drawn', img)
    # cv2.imwrite('output.png', img)

def calibrate_camera(img_pts_list, square_sidelength_m, chess_shape=(7, 9), cam_shape=(1920, 1080)):
    # Generate points in chess calibration frame
    chess_pts = np.zeros((chess_shape[0]*chess_shape[1], 3), np.float32)
    chess_pts[:, :2] = np.mgrid[0:chess_shape[0], 0:chess_shape[1]].T.reshape(-1, 2) * square_sidelength_m

    chess_pts_list = []
    for _ in range(len(img_pts_list)):
        chess_pts_list.append(chess_pts)
    
    cam_rms, cam_intrinsics, cam_dist_coeffs, cam_rvecs, cam_tvecs = cv2.calibrateCamera(chess_pts_list, img_pts_list, cam_shape, None, None, None, None)

    return (cam_rms, cam_intrinsics, cam_dist_coeffs, cam_rvecs, cam_tvecs, chess_pts_list)

def back_project_points(img, K, dist_coeffs, chess_pts_list, corners):
    chess_pts = chess_pts_list[len(chess_pts_list) - 1]

    _ , rvec, tvec = cv2.solvePnP(chess_pts, corners, K, dist_coeffs)

    img_pts = cv2.projectPoints(chess_pts, rvec, tvec, K, dist_coeffs)

    img_undist = cv2.undistort(img, K, dist_coeffs)
  
    for i in range(len(img_pts)):
        img_undist = cv2.circle(img_undist, tuple(img_pts[i].ravel()), 1, (0,0,0), -1)
        cv2.circle()

    return img_undist




if __name__ == "__main__":
    find_chess_corners('Unknown.jpeg', 3)
