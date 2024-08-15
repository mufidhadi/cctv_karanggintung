#!/bin/bash
sudo docker stop mjpeg_vps
sudo docker rm mjpeg_vps
sudo docker run -d --name mjpeg_vps -p 7700:7700 --restart unless-stopped mjpeg:vps
