import cv2 as cv
import face_recognition
import os
import numpy as np
from datetime import datetime
import json
import time

with open("embeddings/name.txt") as f:
    lines = f.read()
line = []
line.extend(lines.split('\n'))   


embeddings = np.loadtxt("embeddings/embeddings.txt")

if not os.path.exists("Attendance.json"):
    with open("Attendance.json", "w") as f:
        json.dump({},f)
with open("Attendance.json","r") as f:
    attendance = json.load(f)

cam = cv.VideoCapture(0)
name = ""
while True:
    ret, frame = cam.read()
    face_location = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_location)
    for (top,right, bottom, left), face_encoding in zip(face_location, face_encodings):
        matches = face_recognition.compare_faces(embeddings, face_encoding)
        if True in matches:
            index = matches.index(True)
            name = line[index]
            if name not in attendance:
                attendance[name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("Attendance.json","w") as f:
                    json.dump(attendance,f)
            cv.rectangle(frame,(left, top),(right,bottom),(0,255,0),2)
            cv.putText(frame, name, (left, top-10), cv.FONT_HERSHEY_SIMPLEX,0.9, (0,255,0),2)
    cv.imshow("frame", frame)
    k = cv.waitKey(1)
    if k == 27:
        break
    
cam.release()
cv.destroyAllWindows()
