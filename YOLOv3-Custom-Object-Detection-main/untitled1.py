# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 21:28:16 2022

@author: user
"""

#import numpy as np
import cv2

cap = cv2.VideoCapture("test_images/soccer.mp4")

while(cap.isOpened()):   #VideoCapture의 성공 유/무를 반환
    frame_pos = cap.get(cv2.CAP_PROP_POS_FRAMES) #현재 프레임 개수 (0번 부터 n번까지 실행)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) #총 프레임 개수 (n+1개 존재)

    ret, frame = cap.read()
    print("convert")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    if (frame_count == frame_pos +1): break

cap.release()  #VideoCapture의 장치를 닫고 메모리를 해제
print("release")
cv2.destroyAllWindows()
print("destory")
