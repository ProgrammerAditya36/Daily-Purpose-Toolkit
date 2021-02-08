import tkinter.font as font
from tkinter import *
import math as m
from math import log as ln
import time
from datetime import datetime
from playsound import playsound
status=True
import os
now = datetime.now()
dir_path = os.path.dirname(os.path.realpath(__file__))


# --------------------------------TKINTER-START---------------------------------------------
alarm = Tk()
alarm.title("alarm")
alarm.geometry("600x400")
alarm.config(bg="#88a5db")

def enter(hrs,minutes,sec,sta):
    global status
    current_time = ""     
    currenttime=0
    if sta !="24":
        if hrs<12 and sta=="PM":
            hrs+=12
        if hrs==12 and sta=="AM":
            hrs=0
    tottime=hrs*3600+minutes*60+sec
    while tottime!=currenttime:        
        current_time = str(datetime.now().time())      
        currenttime=int(current_time[:2])*3600+int(current_time[3:5])*60+int(current_time[6:8])
        if sta!="24":       
            finaltime=str(datetime.now().strftime("%I:%M:%S %p"))
        else:
            finaltime=str(datetime.now().strftime("%H:%M:%S"))
        labelcount=Label(text=finaltime)
        labelcount.grid(sticky="nsew",row=6,column=0,columnspan=3)
        labelcount.config(font=("Tw Cen MT",50),fg="#46484a",bg="#88a5db")
        time.sleep(1)
        alarm.update()
    playsound(dir_path+"\\audio.mp3")
            
        

def enter12():
    global optionsmenu,button12,button24
    button12.destroy()
    button24.destroy()
    labelhours=Label(text="Hours")
    labelhours.grid(sticky="nsew",row=0,column=0)
    options=["AM","PM"]
    entryhours=Entry(alarm,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
    entryhours.grid(sticky="nsew",row=1,column=0)
    labelmin=Label(text="Minutes")
    labelmin.grid(sticky="nsew",row=0,column=1)
    entrymin=Entry(alarm,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
    entrymin.grid(sticky="nsew",row=1,column=1)
    labelsec=Label(text="Seconds")
    labelsec.grid(sticky="nsew",row=0,column=2)
    entrysec=Entry(alarm,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
    entrysec.grid(sticky="nsew",row=1,column=2)
    varampm=StringVar()
    varampm.set("AM")
    optionsmenu=OptionMenu(alarm,varampm,*options)
    optionsmenu.grid(row=2,column=0,columnspan=3,sticky="nswe")
    
    buttonenter=Button(text="Enter",command=lambda:enter(int(entryhours.get()),int(entrymin.get()),int(entrysec.get()),varampm.get()),height=1)
    buttonenter.grid(sticky="nsew",row=4,column=0,columnspan=3)
    components=[entryhours,labelhours,entrymin,labelmin,entrysec,labelsec,optionsmenu,buttonenter]
    for i in components:
        i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
    for i in range(0, alarm.grid_size()[0]):
        alarm.columnconfigure(i, weight=1)
    for i in range(0, alarm.grid_size()[1]):
        alarm.rowconfigure(i, weight=0)
def enter24():
    global optionsmenu,button12,button24
    button12.destroy()
    button24.destroy()
    try:
        optionsmenu.destroy()
    except:
        pass
    labelhours=Label(text="Hours")
    labelhours.grid(sticky="nsew",row=0,column=0)
    
    entryhours=Entry(alarm,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
    entryhours.grid(sticky="nsew",row=1,column=0)
    labelmin=Label(text="Minutes")
    labelmin.grid(sticky="nsew",row=0,column=1)
    entrymin=Entry(alarm,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
    entrymin.grid(sticky="nsew",row=1,column=1)
    labelsec=Label(text="Seconds")
    labelsec.grid(sticky="nsew",row=0,column=2)
    entrysec=Entry(alarm,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
    entrysec.grid(sticky="nsew",row=1,column=2)
    alarm.update()
    
    buttonenter=Button(text="Enter",command=lambda:enter(int(entryhours.get()),int(entrymin.get()),int(entrysec.get()),"24"),height=1)
    buttonenter.grid(sticky="nsew",row=4,column=0,columnspan=3)
    components=[entryhours,labelhours,entrymin,labelmin,entrysec,labelsec,buttonenter]
    for i in components:
        i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
    for i in range(0, alarm.grid_size()[0]):
        alarm.columnconfigure(i, weight=1)
    for i in range(0, alarm.grid_size()[1]):
        alarm.rowconfigure(i, weight=0)
    
    # playsound("F:/aditya and akash/Aditya/Python/Main-Project/alarm/audio.mp3")
mainlabel=Label(text="Choose Time Format:-")
mainlabel.grid(row=0,column=0,columnspan=2,sticky="nsew")
button12=Button(text="12-Hour",command=enter12,height=1)
button12.grid(sticky="nsew",row=3,column=0)
button24=Button(text="24-Hour",command=enter24,height=1)
button24.grid(sticky="nsew",row=3,column=1)
btnclose=Button(alarm,text="Close",command=alarm.destroy)
btnclose.grid(row=100,column=0,columnspan=alarm.grid_size()[0]+1,sticky="nsew")
components=[button12,button24,mainlabel,btnclose]
for i in components:
    i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
for i in range(0, alarm.grid_size()[0]):
    alarm.columnconfigure(i, weight=1)
for i in range(0, alarm.grid_size()[1]):
    alarm.rowconfigure(i, weight=0)

alarm.mainloop()

