
from tkinter import Button, Tk
import os

def callback(filename):
    fname=f"{filename}\{filename}.py"
    os.system(fname)

col,row=0,0
root=Tk()
root.title("All In One Toolkit")
btncalc=Button(root,text="Calculator",command=lambda :callback("Calculator"))
btnconv=Button(root,text="Converter",command=lambda:callback("Converter"))
btnalarm=Button(root,text="Alarm",command=lambda :callback("Alarm"))
btntodolist=Button(root,text="ToDo List",command=lambda:callback("ToDoList"))
btncounter=Button(root,text="Counter",command=lambda :callback("Counter"))
btntimer=Button(root,text="Timer",command=lambda:callback("Timer"))
btnstopwatch=Button(root,text="Stopwatch",command=lambda:callback("stopwatch"))
btnclose=Button(root,text="Close",command=root.destroy)

components=[btncalc,btnconv,btnalarm,btntimer,btncounter,btntodolist,btnstopwatch,btnclose]
for i in components:     
    if col==4:
        row+=1
        col=0   
    col+=1
    i.grid(row=row,column=col)
    i.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",bd=3,width=10,height=3)
for i in range(0, root.grid_size()[0]):
    root.columnconfigure(i, weight=1)
for i in range(0, root.grid_size()[1]):
    root.rowconfigure(i, weight=0)

root.mainloop()