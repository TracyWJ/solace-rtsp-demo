# DACH User Group
## 1. Streaming from Mac Camera
### 1.1 Feeding Camera Data via FFMPEG
```
./ffmpeg -f avfoundation -framerate 30 -video_size 640x480 -i "0" -async 441 -c:v libx264 -preset medium -pix_fmt yuv420p -crf 22 -c:a libfdk_aac -aq 95 -y -f rtsp rtsp://ec2-54-93-139-134.eu-central-1.compute.amazonaws.com:8554/mycamera
```
### 1.2 Recording the Video
```
./ffmpeg -rtsp_transport tcp -i rtsp://ec2-54-93-139-134.eu-central-1.compute.amazonaws.com:8554/mycamera -acodec copy -vcodec copy record.mp4
```
### 1.3 Play the Video
#### VLC
* OutputProxy for Camera: `/Applications/VLC.app/Contents/MacOS/VLC` [rtsp://ec2-3-77-101-249.eu-central-1.compute.amazonaws.com:9999/solace/liveVideoStream/camera](rtsp://ec2-3-77-101-249.eu-central-1.compute.amazonaws.com:9999/solace/liveVideoStream/camera)

#### WebRTC
* OutputProxy for Camera: [http://ec2-3-77-101-249.eu-central-1.compute.amazonaws.com:8000](http://ec2-3-77-101-249.eu-central-1.compute.amazonaws.com:8000)

<img src="pic/aws-outputProxy-camera-eu.png" width="20%" height="20%">

## 2. Streaming from Video File
### 2.1 Feeding Video File via FFMPEG
**FFMEPG process of feeding video file is running on the EC2 instance** `RTSP Server Simulator`

**Skip this step if you don't want to change the input video file**

To change the input video file:
1. Login the EC2 instance:
    ```
   ssh -i "rtsp.pem" ec2-user@ec2-54-93-139-134.eu-central-1.compute.amazonaws.com
   ```
2. CD the directory:
   ```
   cd /home/ec2-user/
   ```
3. Stop the current ffmpeg process:
   ```
   ./stop_send.sh
   ```
4. Start the new ffmpeg process:
   ```
   ./start_<resolution>_to_rtsp.sh
   ```
   
### 2.2 Play the Video
#### VLC
* OutputProxy for Video file: `/Applications/VLC.app/Contents/MacOS/VLC` [rtsp://ec2-3-77-120-143.eu-central-1.compute.amazonaws.com:9999/solace/liveVideoStream/4k](rtsp://ec2-3-77-120-143.eu-central-1.compute.amazonaws.com:9999/solace/liveVideoStream/4k)
  
#### WebRTC
* OutputProxy for Video file: [http://ec2-3-77-120-143.eu-central-1.compute.amazonaws.com:8000](http://ec2-3-77-120-143.eu-central-1.compute.amazonaws.com:8000)

<img src="pic/aws-outputProxy-videofile-eu.png" width="20%" height="20%">

