import argparse
import cv2
import os
import os.path
import subprocess
from functools import partial

CAMERA_FEED_WINDOW = "Camera Feed"
CAMERA_ID = 1

def handle_param_change(pos, param_str, limits_arr):
    unoffsetted_pos = pos - abs(limits_arr[0])
    if unoffsetted_pos > limits_arr[0] and unoffsetted_pos < limits_arr[1]:
        output = subprocess.run(["v4l2-ctl", "-d", f"/dev/video{CAMERA_ID}", f"--set-ctrl={param_str}={unoffsetted_pos}"], capture_output=True)
        # print(f"{param_str} changed to {unoffsetted_pos}, limits=[{limits_arr[0]}, {limits_arr[1]}]")
        print(output.args)

def parse_params_and_limits(camera):
    output = subprocess.run(["v4l2-ctl", "-d", f"/dev/video{CAMERA_ID}", "--list-ctrls"], capture_output=True)
    params = {}
    for line in output.stdout.splitlines():
        line = line.decode("utf-8")
        if 'int' in line:
            parts = line.split(":")
            if len(parts) == 2:
                limits = parts[1].split()
                key = parts[0].replace("(int)", "").strip()
                maxv = None
                minv = None
                valuev = None
                if 'min' in parts[1] and 'max' in parts[1] and 'value' in parts[1]:
                    for limit in limits:
                        if 'min' in limit:
                            minv = limit.split("=")[1]
                        if 'max' in limit:
                            maxv = limit.split("=")[1]
                        if 'value' in limit:
                            valuev = limit.split("=")[1]
                    if maxv and minv and valuev:
                        params[key] = [int(minv), int(maxv), int(valuev)]
    return params

def disable_autos():
    auto_dict = {
        "exposure_auto": 1,
        "white_balance_temperature_auto": 0
    }
    for key, value in auto_dict.items():
        output = subprocess.run(["v4l2-ctl", "-d", f"/dev/video{CAMERA_ID}", f"--set-ctrl={key}={value}"], capture_output=True)
        # print(output.args)

def main(out_param_fname):
    # if not os.path.exists(target_dirname):
    #     os.mkdir(target_dirname)

    cv2.namedWindow(CAMERA_FEED_WINDOW)
    cam = cv2.VideoCapture(CAMERA_ID)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    camera_params = parse_params_and_limits(1)
    for key, value in camera_params.items():
        cv2.createTrackbar(key,
                           CAMERA_FEED_WINDOW,
                           0,
                           value[1] + abs(value[0]),
                           partial(handle_param_change, param_str=key, limits_arr=value))

    # img_counter = 0

    while True:
        disable_autos()
        ret, frame = cam.read()
        if not ret:
            break
        small_frame = cv2.resize(frame, (850, 520))
        cv2.imshow(CAMERA_FEED_WINDOW, small_frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC
            print("Escape hit, closing...")
            break
    #     elif k % 256 == 32:
    #         # SPACE
    #         img_name = "{}/graycode_{}.png".format(target_dirname, str(img_counter).zfill(2))
    #         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #         cv2.imwrite(img_name, gray_frame)
    #         print("{} written!".format(img_name))
    #         img_counter += 1

    # Tear down
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Play image feed and calibrate camera")
    parser.add_argument('-out_param_fname', type=str,
                        default='./cam_params.txt', help='filename name for camera params to be saved [default:"./cam_params.txt"]')

    args = parser.parse_args()
    out_param_fname = args.out_param_fname

    main(out_param_fname)