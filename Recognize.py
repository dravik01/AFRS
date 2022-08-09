from tkinter import *
import datetime
import os
import time
import cv2
import pandas as pd

def take_att():
    global take_attendance
    global name
    take_attendance = Tk()
    take_attendance.title("Detect Face")
    take_attendance.geometry("400x200")
    take_attendance.configure(background= "black")
    btn = Button(take_attendance,text="Detect Face", bg='#0052cc', fg='#ffffff',height = 1, width = 15, font=("times new roman", 12, "bold"),command=recognize_attendence)
    btn.place(x=130,y=35)

#-------------------------
def recognize_attendence():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel"+os.sep+"Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("datas"+os.sep+"data.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name']
    attendance = pd.DataFrame(columns=col_names)

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

            if(conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(
                    ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id, aa]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if(conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown"+os.sep+"Image"+str(noOfFile) +
                            ".jpg", im[y:y+h, x:x+w])
            cv2.putText(im, str(tt), (x, y+h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    # date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    # timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    # Hour, Minute, Second = timeStamp.split(":")
    # fileName = "Attendance"+os.sep+"Attendance_"+date+".csv"
    # attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()

    lbl =Label(take_attendance, text="Faces Detected...",bg="black",fg="white",font = ("times new roman",15,"bold"))
    lbl.place(x=52,y=90)
    take_attendance.after(2010, take_attendance.destroy) 