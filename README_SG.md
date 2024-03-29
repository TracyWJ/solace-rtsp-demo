# India User Group (Deployed on SG)
Solace PubSub+ Broker [Click Here to Open PubSub+ Manager](http://ec2-13-228-169-204.ap-southeast-1.compute.amazonaws.com:8080)
   
## 1. Streaming from Mac Camera
### 1.1 Feeding Camera Data via FFMPEG
```
./ffmpeg -f avfoundation -framerate 30 -video_size 640x480 -i "0" -async 441 -c:v libx264 -preset medium -pix_fmt yuv420p -crf 22 -c:a libfdk_aac -aq 95 -y -f rtsp rtsp://ec2-18-141-78-60.ap-southeast-1.compute.amazonaws.com:8554/mycamera
```
### 1.2 Play the Video
#### VLC
* OutputProxy for Camera: `/Applications/VLC.app/Contents/MacOS/VLC` [rtsp://ec2-13-215-242-183.ap-southeast-1.compute.amazonaws.com:9999/solace/liveVideoStream/camera](rtsp://ec2-13-215-242-183.ap-southeast-1.compute.amazonaws.com:9999/solace/liveVideoStream/camera)

#### WebRTC
* OutputProxy for Camera: [http://ec2-13-215-242-183.ap-southeast-1.compute.amazonaws.com:8000](http://ec2-13-215-242-183.ap-southeast-1.compute.amazonaws.com:8000)
* Scan QR code via the mobile device:
<img src="pic/aws-outputProxy-camera-sg.png" width="20%" height="20%">

### 1.3 Face Recognition
#### Pre-requisites
The following steps are required:
* install python3
* install opencv@3 
* download [faceRecognition](faceRecognition) folder in this repository

#### Run it
```
cd faceRecognition/
python3 webcam_rtsp_cv3.py rtsp://ec2-13-215-242-183.ap-southeast-1.compute.amazonaws.com:9999/solace/liveVideoStream/camera
```

## 2. Streaming from Static 4K Video File
### 2.1 Play the Video
#### VLC
* OutputProxy for Video file: `/Applications/VLC.app/Contents/MacOS/VLC` [rtsp://ec2-52-77-137-232.ap-southeast-1.compute.amazonaws.com:9999/solace/liveVideoStream/4k](rtsp://ec2-52-77-137-232.ap-southeast-1.compute.amazonaws.com:9999/solace/liveVideoStream/4k)
  
#### WebRTC
* OutputProxy for Video file: [http://ec2-52-77-137-232.ap-southeast-1.compute.amazonaws.com:8000](http://ec2-52-77-137-232.ap-southeast-1.compute.amazonaws.com:8000)
* Scan QR code via the mobile device:
<img src="pic/aws-outputProxy-videofile-sg.png" width="20%" height="20%">

