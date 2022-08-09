from tkinter import *
import csv
import cv2
import os
 
ID = None
Name = None
# counting the numbers
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def cap():
    global cap_screen
    global ID
    global Name
    global e1
    global e2
    
    ID = ''
    Name = ''

    cap_screen = Tk()
    cap_screen.title("Capture Image")
    cap_screen.geometry("650x300")
    cap_screen.configure(background= "black")

    wlc = Label(cap_screen, text= "Enter Details",bg="black",fg="white",font = ("times new roman",20,"bold"))
    wlc.place(x=255,y=20)
    l1 = Label(cap_screen, bg="black",fg="white", text = "ID:")
    l1.place(x=225,y=70)
    l2 = Label(cap_screen,bg="black",fg="white", text = "Name:")
    l2.place(x=225,y=100)
    e1 = Entry(cap_screen, textvariable=ID)
    e1.place(x=305,y=70)
    e2 = Entry(cap_screen, textvariable=Name)
    e2.place(x=305,y=100)
    btn = Button(cap_screen,text="Capture Face", bg='#0052cc', fg='#ffffff',height = 1, width = 10, font=("times new roman", 12, "bold"),command=takeImages)
    btn.place(x=285,y=140)
  

def takeImages():
    
    Id = str(e1.get())
    name = str(e2.get())

    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                #incrementing sample number
                sampleNum = sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep +name + "."+Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                #display the frame
                cv2.imshow('frame', img)
            #wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open("datas"+os.sep+"data.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if(is_number(Id)):
            print("Enter Alphabetical Name")
        if(name.isalpha()):
            print("Enter Numeric ID")
    cap_screen.destroy()