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

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    print(len(contours))
    print(i)
    corners = []
    while(i < 4 and i < len(contours)):
        c = contours[i]
        # calculate moments for each contour
        M = cv2.moments(c)

        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
        corners.append((cX,cY))
        # display the image
        i += 1
        print(i)

    return corners

def extract_blue_centroid(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90,50,50])
    upper_blue = np.array([120,255,255])
    mask0 = cv2.inRange(hsv, lower_blue, upper_blue)

    # join my masks
    mask = mask0
    M = cv2.moments(mask)

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    return (cX,cY)

def main():
    circles = cv2.imread('test_imgs/corners.JPG')
    L = extract_red_centroid(circles)
    print(len(L))
    for i in range(len(L)):
        cv2.circle(circles, L[i], 5, [0, 0, 0], -1)
        cv2.imshow("Image",circles)
        cv2.waitKey(0)



if __name__ == "__main__":
    main()
