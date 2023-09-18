#!/bin/bash

ssh -i "../awsCerts/outputProxy_eu.pem" ec2-user@ec2-3-77-120-143.eu-central-1.compute.amazonaws.com << EOF
	sudo docker restart solace-rtsp-connector-out;
	sudo docker restart webrtc_streamer
EOF

