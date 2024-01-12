import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

video_capture = cv2.VideoCapture(0)

shrayash_image = face_recognition.load_image_file("AI_attendance/Backend/photos/biden.jpg")
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

f = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)

while True:
    ret, frame = video_capture.read()
    
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]