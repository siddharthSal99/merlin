from cv import find_chess_pose
from cv import camera_params
from cv import perspective
import cv2
import time
import numpy as np
from cv import visualize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from cv import find_red_pts

CAMERA_ID = 1
CAMERA_WINDOW = "Camera Stream"

def show_image(img):
    img = cv2.resize(img, (960, 480))
    cv2.imshow(CAMERA_WINDOW, img)
    cv2.waitKey(0)

def loop():
    cap = cv2.VideoCapture(CAMERA_ID)
    # chess_img_corners_list = []
    # fig = plt.figure()

    while(True):
        # Set out camera parameters for nice clean image
        camera_params.set_camera_params()

        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break
        
        # cv2.imwrite("test_red.png", frame)
        
        blue_pt = find_red_pts.extract_blue_centroid(frame)
        print("blue_pt: ", blue_pt)
        frame = cv2.circle(frame, (blue_pt[0], blue_pt[1]), 3, (0, 255, 0), -1)
        show_image(frame)
        red_pts = find_red_pts.extract_red_centroid(frame)
        #corners = np.array([(104, 396), (172, 194), (525, 206), (581, 405)])
        if len(red_pts) == 4:
            red_pts = np.array(red_pts)
            rect = perspective.order_points(red_pts)
            
            # test = cv2.circle(test, (rect[2, 0], rect[2, 1]), 4, (0, 0, 255), -1)
            warped_img = perspective.four_point_transform(frame, rect)

            blue_pt = find_red_pts.extract_blue_centroid(warped_img)

            (x, y) = perspective.get_point_in_mm(blue_pt, 1168, 609, warped_img)
            print(x, y)




    # When everything done, release the capture
    # cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    loop()


# test1 = cv2.imread("test1.png")
    # test2 = cv2.imread("test2.png")
    # img_corners, chess_img = find_chess_pose.find_chess_corners(test, (11, 11))
    # img_corners1, chess_img1 = find_chess_pose.find_chess_corners(test1, (11, 11))
    # img_corners2, chess_img2 = find_chess_pose.find_chess_corners(test2, (11, 11))
    # cv2.imshow(CAMERA_WINDOW, chess_img)
    # cv2.waitKey(0)
    # cv2.imshow(CAMERA_WINDOW, chess_img1)
    # cv2.waitKey(0)
    # cv2.imshow(CAMERA_WINDOW, chess_img2)
    # cv2.waitKey(0)
    # chess_img_corners_list = []
    # chess_img_corners_list.append(img_corners)
    # # chess_img_corners_list.append(img_corners1)
    # chess_img_corners_list.append(img_corners2)

    # cam_rms = 10
    # while cam_rms > 3:
    #     cam_rms, cam_intrinsics, cam_dist_coeffs, cam_rvecs, cam_tvecs, chess_pts_list = find_chess_pose.calibrate_camera(chess_img_corners_list, 46, (11, 11), (1920, 1080))
    #     print(cam_rms)
    #     axes_img = visualize.render_axes(frame, cam_intrinsics, cam_dist_coeffs, chess_pts_list, img_corners)

    #     small_img = cv2.resize(axes_img, (960, 480))
    #     cv2.imshow(CAMERA_WINDOW, small_img)
    # cv2.waitKey(0)







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