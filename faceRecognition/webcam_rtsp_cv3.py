import cv2, os
import sys
import logging as log
import datetime as dt
from time import sleep

# Get user supplied values
#rtspURL = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp|timeout;50000000"
# video_capture = cv2.VideoCapture("rtsp://localhost:8554/mystream",cv2.CAP_FFMPEG)
# video_capture = cv2.VideoCapture("rtsp://localhost:9999/solace/liveVideoStream/4k",cv2.CAP_FFMPEG)
video_capture = cv2.VideoCapture("rtsp://ec2-3-77-101-249.eu-central-1.compute.amazonaws.com:9999/solace/liveVideoStream/camera",cv2.CAP_FFMPEG)
anterior = 0
# sleep(5000)

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
