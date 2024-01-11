import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

video_capture = cv2.VideoCapture(0)

shrayash_image = face_recognition.load_image_file("photos/shrayash.jpg")
shrayash_encoding = face_recognition.face_encodings(shrayash_image)[0]
