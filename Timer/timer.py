import tkinter.font as font
from tkinter import *
import math as m
from math import log as ln
import time
import os
from datetime import datetime
from playsound import playsound
dir_path = os.path.dirname(os.path.realpath(__file__))
# --------------------------------TKINTER-START---------------------------------------------
timer = Tk()
timer.title("timer")
timer.geometry("600x400")
timer.config(bg="#88a5db")

labelhours=Label(text="Hours")
labelhours.grid(sticky="nsew",row=0,column=0)

entryhours=Entry(timer,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
entryhours.grid(sticky="nsew",row=0,column=1)
labelmin=Label(text="Minutes")
labelmin.grid(sticky="nsew",row=1,column=0)
entrymin=Entry(timer,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
entrymin.grid(sticky="nsew",row=1,column=1)
labelsec=Label(text="Seconds")
labelsec.grid(sticky="nsew",row=2,column=0)
entrysec=Entry(timer,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
entrysec.grid(sticky="nsew",row=2,column=1)

def enter():
    try:
        hours=int(entryhours.get())
    except:
        hours=0
    try:
        minutes=int(entrymin.get())
    except:
        minutes=0
    try:
        seconds=int(entrysec.get())  
    except:
        seconds=0
    
       
    tottime=(hours)*3600+(minutes)*60+(seconds)      
    for i in range(tottime):        
        s=tottime-i
        hrs=int(s/3600)
        s%=3600
        mnts=int(s/60)
        s%=60
        scnds=s
        
        if hrs>0:
            hrs=str((datetime.strptime(str(hrs),'%I')).time())
            hrs=hrs[:2]
        else:
            hrs="00"
        if mnts>0:
            mnts=str((datetime.strptime(str(mnts),'%M')).time())
            mnts=mnts[3:5]
        else:
            mnts="00"
        if scnds>0:
            scnds=str((datetime.strptime(str(scnds),'%S')).time())
            scnds=scnds[6:8]
        else:
            scnds="00"
        
        finaltime=f"{hrs}:{mnts}:{scnds}"
        labelcount=Label(text=finaltime)
        labelcount.grid(sticky="nsew",row=4,column=0,columnspan=2)
        labelcount.config(font=("Tw Cen MT",100),fg="#46484a",bg="#88a5db")
        timer.update()        
        time.sleep(1)
      
    playsound(dir_path+"\\audio.mp3")
        
button=Button(text="Click",command=enter,height=1)
button.grid(sticky="nsew",row=3,column=1)
resetbtn=Button(text="Reset",height=1)
resetbtn.grid(sticky="nsew",row=3,column=0)
btnclose=Button(timer,text="Close",command=timer.destroy)
btnclose.grid(row=100,column=0,columnspan=timer.grid_size()[0],sticky="nsew")
components=[entrymin,entryhours,entrysec,button,labelmin,labelsec,labelhours,resetbtn,btnclose]
for i in components:
    i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
for i in range(0, timer.grid_size()[0]):
    timer.columnconfigure(i, weight=1)
for i in range(0, timer.grid_size()[1]):
    timer.rowconfigure(i, weight=0)

timer.mainloop()

#01:00:00 00:01:00 00:00:01