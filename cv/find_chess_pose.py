import cv2
import numpy as np

def find_chess_corners(mat, num_corners):
    
    found, corners = cv2.findChessboardCorners(mat, num_corners)
    img = cv2.drawChessboardCorners(mat, (7,9), corners, found)
    cv2.imshow('drawn', img)
    










def main():
    find_chess_corners('Unknown.jpeg', 3)



if __name__ == "__main__":
    main()