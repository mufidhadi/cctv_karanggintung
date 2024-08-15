#!/bin/bash
sudo docker stop mjpeg_raspi
sudo docker rm mjpeg_raspi
sudo docker run -d --name mjpeg_raspi -p 7000:7000 --restart unless-stopped mjpeg:raspi
