import io
import os
from flask import Flask, jsonify, request, render_template
from flask import make_response
from flask_cors import CORS, cross_origin
import json
from pickletools import read_uint1
import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
import cv2

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# load YOLO model
model = torch.hub.load('./yolov5/', 'custom',
                       path='./yolov5/runs/train/weights/best.pt', source='local')

# storing incoming images into POST communication
# all incoming images store in "./images"


def save_image(file):
    file.save('./static/img/' + file.filename)


@app.route('/')
# cors error processing
@cross_origin()
# main page loading
def web():
    return render_template('index.html')

# incomimg images processing with YOLOv5, GET methods for test


@app.route('/test', methods=['GET', 'POST'])
def predict():
    # save incoming images and load images
    if request.method == 'POST':
        file = request.files['file']
        save_image(file)
        train_img = './static/img/' + file.filename
    # for dev & test, it will be remove...
    else:
        train_img = './static/img/' + 'test(iphone).jpg'
    temp = model(train_img)
    print(temp)
    if str(temp).split(" ")[4].split("\n")[0] == "good" or str(temp).split(" ")[4].split("\n")[0] == "goods":
        # result = "<img src='./images/%s'/><h1>좋을 확률이 높음</h1><a href='/'>홈으로</a>" % file.filename
        result = "좋을 확률이 높음"
    else:
        # result = "<img src='./images/%s'/><h1>나쁠 확률이 높음</h1><a href='/'>홈으로</a>" % file.filename
        result = "나쁠 확률이 높음"
    return render_template('result.html', img=file.filename, msg=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)
