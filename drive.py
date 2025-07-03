import socketio
import eventlet
import numpy as np
from flask import Flask
from tensorflow.keras.models import load_model  # ✅ Correct import
import base64
from io import BytesIO
from PIL import Image
import cv2

sio = socketio.Server()
app = Flask(__name__)
speed_limit = 20

def img_preprocess(img):
    img = img[60:135, :, :]                          # crop sky and car hood
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)       # convert to YUV
    img = cv2.GaussianBlur(img, (3, 3), 0)           # reduce noise
    img = cv2.resize(img, (200, 66))                 # resize for model
    img = img / 255.0                                # normalize
    return img

@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        speed = float(data['speed'])
        image = Image.open(BytesIO(base64.b64decode(data['image'])))
        image = np.asarray(image)
        image = img_preprocess(image)
        image = np.array([image])
        steering_angle = float(model.predict(image))
        throttle = 1.0 - speed / speed_limit
        print(f'Steering: {steering_angle:.4f}, Throttle: {throttle:.4f}, Speed: {speed:.2f}')
        send_control(steering_angle, throttle)

@sio.on('connect')
def connect(sid, environ):
    print('✅ Simulator connected.')
    send_control(0, 0)

def send_control(steering_angle, throttle):
    sio.emit('steer', data={
        'steering_angle': str(steering_angle),
        'throttle': str(throttle)
    })

if __name__ == '__main__':
    model = load_model('model.h5', compile=False)  
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)

