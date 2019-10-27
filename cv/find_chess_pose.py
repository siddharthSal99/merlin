import cv2
import numpy as np

<<<<<<< HEAD
def find_chess_corners(mat, num_corners):
    
    found, corners = cv2.findChessboardCorners(mat, num_corners)
    img = cv2.drawChessboardCorners(mat, (7,9), corners, found)
    cv2.imshow('drawn', img)
    










def main():
    find_chess_corners('Unknown.jpeg', 3)


=======
def find_chess_corners(img, corners_dim=(7, 9)):
    found, corners = cv2.findChessboardCorners(img, corners_dim)
    return cv2.drawChessboardCorners(img, corners_dim, corners, found)
    # cv2.imshow('drawn', img)
    # cv2.imwrite('output.png', img)
>>>>>>> 6a5f8c7f8fce2e5af3739d6b91d81ff8a10e4e48

if __name__ == "__main__":
    find_chess_corners('Unknown.jpeg', 3)
