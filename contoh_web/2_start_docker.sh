#!/bin/bash

sudo docker stop web_cctv
sudo docker rm web_cctv

sudo docker run -d --name web_cctv -p 8080:8080 --restart unless-stopped web_cctv