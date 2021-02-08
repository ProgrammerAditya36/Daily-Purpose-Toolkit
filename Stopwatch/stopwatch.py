import tkinter.font as font
from tkinter import *
import math as m
from math import log as ln
import time
from datetime import datetime
from playsound import playsound
flaglist=[]
# --------------------------------TKINTER-START---------------------------------------------
stopwatch = Tk()
stopwatch.title("stopwatch")
stopwatch.geometry("600x400")
stopwatch.config(bg="#88a5db")
hrs,mnts,scnds="00","00","00"
finaltime=f"{hrs}:{mnts}:{scnds}"
labelcount=Label(text=finaltime)
labelcount.grid(sticky="nsew",row=5,column=0,columnspan=2)
labelcount.config(font=("Tw Cen MT",100),fg="#46484a",bg="#88a5db")
status=True

def enter():
       global status,mnts,hrs,scnds ,finaltime
       seconds=int(scnds)
       minutes=int(mnts)
       hours=int(hrs)
       status=True
       while status==True:
            seconds+=1            
            if seconds==60:
               minutes+=1
               seconds=0
               if minutes==60:
                   hours+=1
                   minutes=0
            if seconds<10:
               scnds="0"+str(seconds)
            else:
                scnds=str(seconds)
            if minutes<10:
               mnts="0"+str(minutes)
            else:
                mnts=str(minutes)
            if hours<10:
               hrs="0"+str(hours)
            else:
                hrs=str(hours)
            finaltime=f"{hrs}:{mnts}:{scnds}"
            labelcount=Label(text=finaltime)
            labelcount.grid(sticky="nsew",row=5,column=0,columnspan=2)
            labelcount.config(font=("Tw Cen MT",100),fg="#46484a",bg="#88a5db")
            time.sleep(1)
            stopwatch.update()
        
def pause():
    global status,mnts,hrs,scnds,labelcount
    labelcount.destroy()
    status = False
def reset():
        global status,mnts,hrs,scnds,labelcount,finaltime
        strr="00"
        finaltime=f"{strr}:{strr}:{strr}"
        labelcount=Label(text=finaltime)
        labelcount.grid(sticky="nsew",row=5,column=0,columnspan=2)
        labelcount.config(font=("Tw Cen MT",100),fg="#46484a",bg="#88a5db")
        status = False
def flag():
    global status,mnts,hrs,scnds,labelcount,finaltime
    flaglist.append(finaltime)
    labellist=Label(text=str(flaglist[len(flaglist)-1]))
    labellist.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db")
    labellist.grid(sticky="nsew",row=len(flaglist)+6,column=0,columnspan=3)
        
        
button=Button(text="Click",command=enter,height=1)
button.grid(sticky="nsew",row=3,column=1)
resetbtn=Button(text="Reset",height=1,command=reset)
resetbtn.grid(sticky="nsew",row=3,column=0)
pausebtn=Button(text="Pause",height=1,command=pause)
pausebtn.grid(sticky="nsew",row=4,column=0)
flagbtn=Button(text="Flag",height=1,command=flag)
flagbtn.grid(sticky="nsew",row=4,column=1)
btnclose=Button(stopwatch,text="Close",command=stopwatch.destroy)
btnclose.grid(row=100,column=0,columnspan=stopwatch.grid_size()[0],sticky="nsew")

components=[button,resetbtn,pausebtn,flagbtn,btnclose]
for i in components:
    i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
for i in range(0, stopwatch.grid_size()[0]):
    stopwatch.columnconfigure(i, weight=1)
for i in range(0, stopwatch.grid_size()[1]):
    stopwatch.rowconfigure(i, weight=0)

stopwatch.mainloop()

#01:00:00 00:01:00 00:00:01