import math
import cv2
import numpy as np

def readFileWriteMotion():
    delta_thresh = 25
    min_area = 0
    video = cv2.VideoCapture(r'E:/new/testProjectMult/output.mov', cv2.CAP_ANY)
    ok, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("motion.mov", fourcc, 25, (w, h))
    while (ok):
        ok1,frame1 = ok,frame
        ok, frame = video.read()
        if not(ok):
            break
        prev_gray = gray.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        frameDelta = cv2.absdiff(gray, prev_gray)

        thresh = cv2.threshold(frameDelta, delta_thresh, 255,
                               cv2.THRESH_BINARY)[1]
        (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion_detected = False
        cv2.imshow('img', frame1)
        for c in cnts:
            if cv2.contourArea(c) > min_area:
                motion_detected = True
                break
            else:
                motion_detected = False
        if (motion_detected):
            video_writer.write(frame1)
        cv2.waitKey(5)
    video.release()
    cv2.destroyAllWindows()

readFileWriteMotion()