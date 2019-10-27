from cv import find_chess_pose
from cv import camera_params
import cv2
import time
from cv import visualize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

CAMERA_ID = 1
CAMERA_WINDOW = "Camera Stream"

def loop():
    cap = cv2.VideoCapture(CAMERA_ID)
    chess_img_corners_list = []
    fig = plt.figure()

    camera_params.set_camera_params()
    ret, frame = cap.read()
    cv2.imwrite("test2.png", frame)
    
    test = cv2.imread("test.png")
    test1 = cv2.imread("test1.png")
    test2 = cv2.imread("test2.png")
    img_corners, chess_img = find_chess_pose.find_chess_corners(test, (11, 11))
    img_corners1, chess_img1 = find_chess_pose.find_chess_corners(test1, (11, 11))
    img_corners2, chess_img2 = find_chess_pose.find_chess_corners(test2, (11, 11))
    cv2.imshow(CAMERA_WINDOW, chess_img)
    cv2.waitKey(0)
    cv2.imshow(CAMERA_WINDOW, chess_img1)
    cv2.waitKey(0)
    cv2.imshow(CAMERA_WINDOW, chess_img2)
    cv2.waitKey(0)
    chess_img_corners_list = []
    chess_img_corners_list.append(img_corners)
    # chess_img_corners_list.append(img_corners1)
    chess_img_corners_list.append(img_corners2)

    cam_rms = 10
    while cam_rms > 3:
        cam_rms, cam_intrinsics, cam_dist_coeffs, cam_rvecs, cam_tvecs, chess_pts_list = find_chess_pose.calibrate_camera(chess_img_corners_list, 46, (11, 11), (1920, 1080))
        print(cam_rms)
        axes_img = visualize.render_axes(frame, cam_intrinsics, cam_dist_coeffs, chess_pts_list, img_corners)

        small_img = cv2.resize(axes_img, (960, 480))
        cv2.imshow(CAMERA_WINDOW, small_img)
    cv2.waitKey(0)

    # while(True):
    #     # Set out camera parameters for nice clean image
    #     camera_params.set_camera_params()

    #     # Capture frame-by-frame
    #     ret, frame = cap.read()
    #     if not ret:
    #         break

    #     # turn grayscale
    #     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #     # find and draw chessgrid
    #     img_corners, chess_img = find_chess_pose.find_chess_corners(frame, (11, 11))
    #     chess_img_corners_list.append(img_corners)

    #     # Calibrate camera
    #     (cam_rms, cam_intrinsics, 
    #     cam_dist_coeffs, 
    #     cam_rvecs, 
    #     cam_tvecs, 
    #     chess_pts_list) = find_chess_pose.calibrate_camera(chess_img_corners_list, 46, (11, 11), (1920, 1080))
    #     print(cam_rms)
        
    #     # visualize.calibrate_plot(cam_rvecs, cam_tvecs, chess_pts_list, fig)
    #     axes_img = visualize.render_axes(frame, cam_intrinsics, cam_dist_coeffs, chess_pts_list, img_corners)

    #     # resize
    #     small = cv2.resize(axes_img, (920, 640))

    #     # Display the resulting frame
    #     cv2.imshow(CAMERA_WINDOW, small)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
        
    #     time.sleep(1)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    loop()