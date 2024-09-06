import cv2
import os
import mysql.connector
import tkinter
from tkinter import messagebox
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

def valid(roll):
    cur.execute("select roll from students")
    result = cur.fetchall()
    for i in result:
        if i[0] == roll:
            return False
    return True

def add_data(name, roll):
    valid(roll)
    try:
        cur.execute("create table students (name varchar(20),roll varchar(20), class varchar(30))")
    except Exception as e:
        print(e)
    if valid(roll):
        values = (name, roll,"AIDS")
        cur.execute("insert into students values(%s,%s,%s )", values)
        db.commit()
        showpopup("Student registered")
        sys.exit()
    else:
        showpopup("Student already registered")
        sys.exist()

cam = cv2.VideoCapture(0)

if not os.path.exists("dataset"):
    os.makedirs("dataset")
def main1(name,roll):
    while True:
        ref, frame = cam.read()
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == 32:
            if valid(roll):
                filename = "dataset/"+str(roll)+".jpg"
                cv2.imwrite(filename, frame)
                add_data(name, roll)
                break
            else:
                showpopup("Student already registered")
                break

    cam.release()
    cv2.destroyAllWindows()
    cur.close()

