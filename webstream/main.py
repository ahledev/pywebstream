from imutils.video import VideoStream
from flask import Reponse
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2

app = Flask(__name__)
vs = VideoStream(src=0).start()
time.sleep(2.0)
