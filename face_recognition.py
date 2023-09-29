import cv2 as cv
import face_recognition

img1 = cv.imread("th.png")
img2 = cv.imread("th1.jpg")


location1 = face_recognition.face_locations(img1)
location2 = face_recognition.face_locations(img2)

encoding1 = face_recognition.face_encodings(img1,location1)[0]
encoding2 = face_recognition.face_encodings(img2, location2)[0]
 
result = face_recognition.compare_faces([encoding1],encoding2)  #returns true if face matches or vice-versa
print(result)
