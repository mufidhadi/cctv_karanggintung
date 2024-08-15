from flask import Flask, Response, request
import cv2
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

target_height = 480
target_height = 360
target_height = 240

# Function to generate MJPEG frames from RTSP stream
def generate_frames(rtsp_url,use_small=True):
    cap = cv2.VideoCapture(rtsp_url)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if use_small:
            f_w = frame.shape[1]
            f_h = frame.shape[0]

            resize_ratio = target_height / f_h
            new_width = int(f_w * resize_ratio)
            frame = cv2.resize(frame, (new_width, target_height))

        # Convert the frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    cap.release()

@app.route('/video_feed')
def video_feed():
    source = request.args.get('source', 0)
    return Response(generate_frames(source, True), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_full')
def video_feed_full():
    source = request.args.get('source', 0)
    return Response(generate_frames(source, False), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
