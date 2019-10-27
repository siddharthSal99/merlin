from cv import find_chess_pose
from cv import camera_params
import cv2
import time
from cv import visualize as booty
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

CAMERA_ID = 1
CAMERA_WINDOW = "Camera Stream"

def loop():

    cap = cv2.VideoCapture(CAMERA_ID)
    chess_img_corners_list = []
    fig = plt.figure()
    while(True):
        # Set out camera parameters for nice clean image
        camera_params.set_camera_params()

        # Capture frame-by-frame
        ret, frame = cap.read()

        # turn grayscale
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # find and draw chessgrid
        img_corners, chess_img = find_chess_pose.find_chess_corners(frame, (9, 7))
        chess_img_corners_list.append(img_corners)

        # Calibrate camera
        cam_rms, cam_intrinsics, cam_dist_coeffs, cam_rvecs, cam_tvecs, chess_pts_list = find_chess_pose.calibrate_camera(chess_img_corners_list, 12, (9, 7), (1920, 1080))
        #print(rms)
        
        booty.calibrate(cam_rvecs, cam_tvecs, chess_pts_list, fig)
        # resize
        small = cv2.resize(chess_img, (920, 640))

        # Display the resulting frame
        cv2.imshow(CAMERA_WINDOW, small)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        time.sleep(10)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    loop()