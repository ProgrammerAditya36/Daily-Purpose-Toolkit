import tkinter.font as font
from tkinter import *
import math as m
from math import log as ln

# --------------------------------TKINTER-START---------------------------------------------
counter = Tk()
counter.title("Counter")
counter.geometry("600x400")
counter.config(bg="#88a5db")
step=1
count=0
labelcount=Label(text=count)
labelcount.grid(sticky="nsew",row=1,column=0,columnspan=2)
labelcount.config(font=("Tw Cen MT",100),fg="#46484a",bg="#88a5db")
labelstv=Label(text="Enter Step Value")
labelstv.grid(sticky="nsew",row=4,column=0)
entry=Entry(counter,text="Enter Step Value",justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
entry.grid(sticky="nsew",row=4,column=1)
def enter():
    global count,labelcount
    try:
        step=int(entry.get())
    except:
        step=1
    count+=step
    labelcount=Label(text=count)
    labelcount.config(font=("Tw Cen MT",100),fg="#46484a",bg="#88a5db")
    labelcount.grid(sticky="nsew",row=1,column=0,columnspan=3)
def reset():
    global step,count
    step=1
    count=0
    labelcount.config(text=0)
    labelcount.grid(sticky="nsew",row=1,column=0,columnspan=3)
    entry.delete(0,END)
button=Button(text="Click",command=enter,height=1)
button.grid(sticky="nsew",row=3,column=1)
resetbtn=Button(text="Reset",command=reset,height=1)
resetbtn.grid(sticky="nsew",row=3,column=0)
btnclose=Button(counter,text="Close",command=counter.destroy)
btnclose.grid(row=100,column=0,columnspan=counter.grid_size()[0],sticky="nsew")
components=[entry,button,labelstv,resetbtn,btnclose]
btnclose=Button(counter,text="Close",command=counter.destroy)
btnclose.grid(row=100,column=0,columnspan=counter.grid_size()[0],sticky="nsew")
btnclose.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
for i in components:
    i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
for i in range(0, counter.grid_size()[0]):
    counter.columnconfigure(i, weight=1)
for i in range(0, counter.grid_size()[1]):
    counter.rowconfigure(i, weight=0)

counter.mainloop()
