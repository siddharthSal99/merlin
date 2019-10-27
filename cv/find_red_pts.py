import cv2
import numpy as np

def extract_red_centroid(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # join my masks
    mask = mask0+mask1
    cv2.imshow("mask",mask)
    M = cv2.moments(mask)

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    return (cX,cY)


def main():
    circles = cv2.imread('test_imgs/wood_sim.JPG')
    (cX,cY) = extract_red_centroid(circles)
    cv2.circle(circles, (cX, cY), 5, [0, 0, 0], -1)
    cv2.imshow("Image",circles)
    cv2.waitKey(0)



if __name__ == "__main__":
    main()
