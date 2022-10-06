# -*- coding: utf-8 -*-
#import flasks libraries
from flask import Flask, render_template, request, jsonify, url_for, redirect, flash, Response, send_file
from flask_socketio import SocketIO, emit
import webbrowser
from threading import Timer
from recognise import predictor,get_frame
from out import Videocamera


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


def gen(out):
    while True:
        frame=out.g_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image\jpeg\r\n\r\n' + frame
        + b'\r\n\r\n')
@app.route('/Video_feed')
def Video_feed():
    return Response(gen(Videocamera()),
    mimetype='multipart/x-mixed-replace; boundary=frame')


"""
def gen(xzy):
        frame=get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image\png\r\n\r\n' + frame
        + b'\r\n\r\n')

@app.route('/VideoCamera')
def VideoCamera():
    return Response(gen(predictor()),
    mimetype='multipart/x-mixed-replace; boundary=frame')
"""
if __name__ == '__main__':
    Timer(1,lambda: webbrowser.open_new("http://127.0.0.1:5000/")).start()
    socketio.run(app)