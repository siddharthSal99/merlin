import numpy as np
import cv2
import find_chess_pose as f

cap = cv2.VideoCapture(0)
cap.set(15, -8.0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(frame.shape)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    small = cv2.resize(frame, (920, 640))
    f.find_chess_corners(small, (9,7))
    # Display the resulting frame
    cv2.imshow('frame',small)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()