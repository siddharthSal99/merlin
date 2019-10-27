from cv import find_chess_pose
from cv import camera_params
import cv2
import time

CAMERA_ID = 1
CAMERA_WINDOW = "Camera Stream"

def loop():

    cap = cv2.VideoCapture(CAMERA_ID)
    chess_img_corners_list = []

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
        rms = find_chess_pose.calibrate_camera(chess_img_corners_list, 50, (9, 7), (1920, 1080))
        print(rms)

        # resize
        small = cv2.resize(chess_img, (920, 640))

        # Display the resulting frame
        cv2.imshow(CAMERA_WINDOW, small)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(1)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    loop()