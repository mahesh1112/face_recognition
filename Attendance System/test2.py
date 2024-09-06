import cv2 as cv
import face_recognition
import numpy as np
from datetime import datetime
import mysql.connector
import tkinter
from tkinter import messagebox
# from dbms import Ui_MainWindow
import sys

root = tkinter.Tk()
root.withdraw()

def showpopup(message):
    messagebox.showinfo("info",message)
    root.mainloop()
    




db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password",
    database = "Attendance"
)
cur = db.cursor()
def mark_attendance(roll,sub,date):
    day = datetime.now().day
    sub = f"{sub}{day}"
    def valid():
        cur.execute(f"select roll from {sub}")
        result = cur.fetchall()
        for i in result:
            if i[0] == roll:
                return False
        return True

    
    try:
        cur.execute(f"create table {sub} (roll varchar(20), time varchar(30))")
    except Exception as e:
        pass
    values = (roll,date)
    if valid():
        cur.execute(f"insert into {sub} values(%s,%s)",values)
        db.commit()
        showpopup("Attendance marked")
        cur.close()
        sys.exit()
       
    else:
        showpopup("Attendance already marked.")
        cur.close()
        sys.exit()




def main1(name,sub):
    cam = cv.VideoCapture(0)
    
    img = face_recognition.load_image_file(f"dataset\{name}.jpg")
    face_location1 = face_recognition.face_locations(img)
    face_encoding1 = face_recognition.face_encodings(img, face_location1)
    while True:
        ret, frame = cam.read()
        #img = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        face_location = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_location)
        for (top,right, bottom, left), face_encoding in zip(face_location, face_encodings):
            matches = face_recognition.compare_faces(face_encoding1, face_encoding)
            cv.rectangle(frame,(left, top),(right,bottom),(0,255,0),2)
            if True in matches:
                cv.putText(frame, name, (left, top-10), cv.FONT_HERSHEY_SIMPLEX,0.9, (0,255,0),2)
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                mark_attendance(name, sub,date)
                sys.exit()
        cv.imshow("frame", frame)
        k = cv.waitKey(1)
        if k == 27:
            break

    cam.release()
    cv.destroyAllWindows()
