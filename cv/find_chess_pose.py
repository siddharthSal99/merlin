import cv2
import numpy as np

def find_chess_corners(img, corners_dim=(7, 9)):
    found, corners = cv2.findChessboardCorners(img, corners_dim)
    return cv2.drawChessboardCorners(img, corners_dim, corners, found)
    # cv2.imshow('drawn', img)
    # cv2.imwrite('output.png', img)

if __name__ == "__main__":
    find_chess_corners('Unknown.jpeg', 3)
