import cv2
import numpy as np

def find_chess_corners(file_name, num_corners):
    c = cv2.imread(file_name)
    found, corners = cv2.findChessboardCorners(c, (7,9))
    img = cv2.drawChessboardCorners(c, (7,9), corners, found)
    cv2.imshow('drawn', img)
    cv2.imwrite('output.png', img)










def main():
    find_chess_corners('Unknown.jpeg', 3)



if __name__ == "__main__":
    main()