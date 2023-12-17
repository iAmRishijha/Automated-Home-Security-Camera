import os
import cv2 as cv
import face_recognition
import subprocess


img_list = os.listdir("media")

encodings = []
for img in img_list:
    print("Encoding "+img+" ...")
    loaded_img = face_recognition.load_image_file("media\\"+img)
    img_encoding = face_recognition.face_encodings(loaded_img)[0]
    encodings.append(img_encoding)

def compare(unknown_face_encodings):
    for unknown_encodings in unknown_face_encodings:
        results = face_recognition.compare_faces(encodings, unknown_encodings)
        if True in results:
            print("Face Match")
        else:
            print("Stranger")
            subprocess.run(["python", "mail.py"])
        

video = cv.VideoCapture(0)
no_of_frames = 0
print("Turning Camera On...")
while True:
    ret, frame = video.read()
    frame = cv.flip(frame,1)
    frame_copy = frame.copy()
    frame_copy = cv.cvtColor(frame_copy,cv.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(frame_copy)
    
    if(len(face_locations)!=0):
        no_of_frames+=1
        if(no_of_frames>10):
            no_of_frames=0
            unknown_face_encodings = face_recognition.face_encodings(frame_copy,face_locations)
            compare(unknown_face_encodings)
    else:
        no_of_frames=0

    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()