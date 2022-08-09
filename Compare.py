from tkinter import *
import sys, os
import csv

def cmp_screen():
    global comp_screen
    global lbl

    comp_screen = Tk()
    comp_screen.geometry("450x200")
    comp_screen.title("train Image")
    comp_screen.configure(background= "black")
    strat = Button(comp_screen,text="Click to get absent students details", bg='#0052cc', fg='#ffffff',height = 1, width = 30, font=("times new roman", 15, "bold"),command=get)
    strat.place(x=42,y=35)

def get():
    # Read in the original and new filecd
    stuDetails = open('Attendance\StudentRecord.csv','r+')
    stuAttendance = open('Attendance\Attendance_2020-02-28.csv','r')

    #in new but not in orig
    bigb = set(stuDetails) - set(stuAttendance)

    print(bigb)
    # Write to output file    
    with open('absent.csv', 'w') as file_out:
        for line in bigb:
            file_out.write(line)

    #close the files  
    stuDetails.close()    
    stuAttendance.close()    
    file_out.close()

    lbl =Label(comp_screen, text="Abesent Students List Genrated...",bg="black",fg="white",font = ("times new roman",15,"bold"))
    lbl.place(x=78,y=120)
    comp_screen.after(2010, comp_screen.destroy) 

