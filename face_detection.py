from tkinter import *
import os
import check_camera
import Capture_Image
import Train_Image
import Recognize
import Compare


def checkCamera():
    check_camera.camer()

def CaptureFaces():
    Capture_Image.cap()

def Trainimages():
    Train_Image.tra_screen()

def RecognizeFaces():
    Recognize.take_att()

def ExitScreen():
    main_screen.destroy()
    
    


def main_Menu():
    global main_screen
    main_screen = Tk()
    main_screen.attributes('-fullscreen', True)
    main_screen.title("face detection and recognition")
    main_screen.configure(background= "black")

    w = Label(main_screen, text="face detection and recognition",bg="black",fg="white",font = ("times new roman",40,"bold"))
    w.place(x=400,y=20)

    myFont = font=("times new roman", 20, "bold")

    checkCamera1 = Button(text="Check Camera", bg='#0052cc', fg='#ffffff',height = 3,width = 20,font= myFont, command = checkCamera).place(x=150, y=200)
    captureFace = Button(text="Register Face", bg='#0052cc', fg='#ffffff',height = 3,width = 20,font= myFont, command=CaptureFaces).place(x=150, y=350)
    # checkAttendance = Button(text="Check Attendance", bg='#0052cc', fg='#ffffff',height = 3,width = 20,font= myFont, command=getDetails).place(x=150, y=500)
    TrainImage = Button(text="Train Images", bg='#0052cc', fg='#ffffff',height = 3,width = 20,font= myFont, command=Trainimages).place(x=900, y=200)
    RecognizeFace = Button(text="Detect Face", bg='#0052cc', fg='#ffffff',height = 3,width = 20,font= myFont, command=RecognizeFaces).place(x=900, y=350)
    exitScreen = Button(text="Exit", bg='#0052cc', fg='#ffffff',height = 3,width = 20,font= myFont, command=ExitScreen).place(x=900, y=500)

    main_screen.mainloop()

main_Menu() 