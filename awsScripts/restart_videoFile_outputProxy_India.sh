#!/bin/bash

ssh -i "../awsCerts/outputProxy_india.pem" ec2-user@ec2-3-111-203-34.ap-south-1.compute.amazonaws.com << EOF
	sudo docker restart solace-rtsp-connector-out;
	sudo docker restart webrtc_streamer
EOF

