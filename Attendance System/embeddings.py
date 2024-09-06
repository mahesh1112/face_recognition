import face_recognition 
import os
import numpy as np

if not os.path.exists("embeddings"):
    os.makedirs("embeddings")

image_name = os.listdir("dataset")
image_paths = [os.path.join("dataset",f) for f in os.listdir("dataset")]
images = []
for i in image_paths:
    image = face_recognition.load_image_file(i)
    images.append(image)

embeddings = []
names = []
count = 0
for image in images:
    face_location = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_location)
    if len(face_encodings) == 1:
        embeddings.append(face_encodings[0])
        names.append(image_name[count].split(".")[0])
        count+=1
    
np.savetxt("embeddings/embeddings.txt", embeddings)
with open("embeddings/name.txt", "w") as f:
    for i in names:
        f.write(i)
        f.write("\n")
