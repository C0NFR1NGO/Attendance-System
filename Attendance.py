import cv2
import numpy as np
import face_recognition
import os
import datetime


Attendance = open("Attendance.csv", 'a')

path = 'ImagesBasic'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
cap = cv2.VideoCapture(0)


marked_this_session = set()


while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    
    facesCurFrame = face_recognition.face_locations(imgS, model="hog")
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            
            
            if name not in marked_this_session:
                now = datetime.datetime.now()
                timeStr = now.strftime('%H:%M:%S')
                dateStr = now.strftime('%d-%m-%Y')
                
                Attendance.write(f'{name}, {dateStr}, {timeStr}\n')
                Attendance.flush() 
                
                
                marked_this_session.add(name)
                print(f"Attendance marked for {name} at {timeStr}")

            y1, x2, y2, x1 = map(lambda x: x*4, faceLoc)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), 1)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)