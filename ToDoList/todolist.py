import tkinter.font as font
from tkinter import *
import math as m
from math import log as ln
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")


# --------------------------------TKINTER-START---------------------------------------------
todolist = Tk()
todolist.title("todolist")
todolist.geometry("600x400")
todolist.config(bg="#88a5db")
step=""
count=[]
labelcount=Label(text=d1)
labelcount.grid(sticky="nsew",row=0,column=0,columnspan=2)
labelcount.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db")
labelstv=Label(text="Enter Item")
labelstv.grid(sticky="nsew",row=1,column=0)
entry=Entry(todolist,justify=CENTER,relief=RAISED,bd=4,state=NORMAL)
entry.grid(sticky="nsew",row=1,column=1)
def enter():    
    global count,labelcount,labellist
    try:
        step=(entry.get())
    except:
        step=1
    count.append(step)
    labellist=Label(text="• "+str(count[len(count)-1]))
    labellist.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db")
    labellist.grid(sticky="nsew",row=len(count)+5,column=0,columnspan=3)
    entry.delete(0,END)
button=Button(text="Add",command=enter,height=1)
button.grid(sticky="nsew",row=3,column=0,columnspan=2)
btnclose=Button(todolist,text="Close",command=todolist.destroy)
btnclose.grid(row=100,column=0,columnspan=todolist.grid_size()[0],sticky="nsew")
components=[entry,button,labelstv,btnclose]
for i in components:
    i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)
for i in range(0, todolist.grid_size()[0]):
    todolist.columnconfigure(i, weight=1)
for i in range(0, todolist.grid_size()[1]):
    todolist.rowconfigure(i, weight=0)

todolist.mainloop()
