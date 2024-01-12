import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

video_capture = cv2.VideoCapture(0)

shrayash_image = face_recognition.load_image_file("biden.jpg")
shrayash_encoding = face_recognition.face_encodings(shrayash_image)[0]

known_face_encoding = [shrayash_encoding]

known_face_names = ["biden"]

students = known_face_names.copy()

face_locations = []
face_encoding = []
face_names = []
s = True 

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

