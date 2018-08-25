import cv2
import time
import numpy as np
import multiprocessing

cap=cv2.VideoCapture(0)#调取摄像头
#cap=cv2.VideoCapture('test.avi')#读取本地视频

while(cap.isOpened()):
    # Capture frame-by-frame
    ret,frame=cap.read()
 
    print(ret)
    # Our operations on the frame come here
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
 
    # Display the resulting frame
    cv2.imshow('frame',gray)
    #cv2.imshow('frame',frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
