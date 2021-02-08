import tkinter.font as font
from tkinter import *
import math as m
from math import log as ln

# --------------------------------TKINTER-START---------------------------------------------
calculator = Tk()
calculator.title("Calculator")
calculator.geometry("400x600")
calculator.config(bg="#000")

# --------------------------------Variables---------------------------------------------
r = 5
calculate = " "
show = " "



# --------------------------------Functions-Start---------------------------------------------
def charenter(num):
    global calculate
    calculate = entry.get() + str(num)
    show = entry.get() + str(num)
    entry.delete(0, END)
    entry.insert(0, show)



def equal():
    global calculate
    calculate = str(calculate)
    calculate = calculate.replace("x", "*")
    calculate = calculate.replace("cosec", "1/sin")
    calculate = calculate.replace("sec", "1/cos")
    calculate = calculate.replace("cot", "1/tan")
    calculate = calculate.replace("sin", "m.sin(")
    calculate = calculate.replace("cos", "m.cos(")
    calculate = calculate.replace("tan", "m.tan(")
    calculate = calculate.replace("rad", ")")
    calculate = calculate.replace("°", "*m.pi/180)")
    calculate = calculate.replace("^", "**")
    calculate = calculate.replace("log", "m.log10")
    calculate = calculate.replace("ln", "m.log")
    calculate = calculate.replace("e", str(m.e))
    calculate = calculate.replace("π", str(m.pi))

    if "√" in calculate:
        calculate = calculate.replace("√(", "m.pow(")
        calculate = calculate.replace(")", ",0.5)")

    
    try:
        final=round(eval(calculate),8)
    except:
        final = "INVALID INPUT"
    entry.delete(0, END)
    entry.insert(0, final)


def clear():
    global calculate

    main = entry.get()
    if main != "INVALID INPUT":
        show = main[:len(main) - 1]
        calculate = main[:len(main) - 1]
        entry.delete(0, END)
        entry.insert(0, show)


def allclear():
    global calculate
    calculate = ""
    show = ""
    entry.delete(0, END)
    entry.insert(0, show)


# --------------------------------Buttons---------------------------------------------
# ====================Column0================
btncosec = Button(calculator, bg="#22aa7a", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20),
                  text='cosec', command=lambda: charenter('cosec'))
btnsin = Button(calculator, bg="#22aa7a", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='sin',
                command=lambda: charenter('sin'))
btnln = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='ln',
                command=lambda: charenter('ln'))
btn7 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=7,
              command=lambda: charenter(7))
btn4 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=4,
              command=lambda: charenter(4))
btn1 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=1,
              command=lambda: charenter(1))
btnob = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='(',
               command=lambda: charenter('('))

btncosec.grid(sticky="nsew", row=r-3, column=0)
btnsin.grid(sticky="nsew", row=r-2, column=0)
btnln.grid(sticky="nsew", row=r-1, column=0)
btn7.grid(sticky="nsew", row=r, column=0)
btn4.grid(sticky="nsew", row=r + 1, column=0)
btn1.grid(sticky="nsew", row=r + 2, column=0)
btnob.grid(sticky="nsew", row=r + 3, column=0)
# ====================Column1================
btnsec = Button(calculator, bg="#22aa7a", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='sec',
                command=lambda: charenter('sec'))
btncos = Button(calculator, bg="#22aa7a", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='cos',
                command=lambda: charenter('cos'))
btnlog = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='log',
                command=lambda: charenter('log'))
btn8 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=8,
              command=lambda: charenter(8))
btn5 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=5,
              command=lambda: charenter(5))
btn2 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=2,
              command=lambda: charenter(2))
btn0 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=0,
              command=lambda: charenter(0))

btnsec.grid(sticky="nsew", row=r-3, column=1)
btncos.grid(sticky="nsew", row=r-2, column=1)
btnlog.grid(sticky="nsew", row=r-1,column=1)
btn8.grid(sticky="nsew", row=r, column=1)
btn5.grid(sticky="nsew", row=r + 1, column=1)
btn2.grid(sticky="nsew", row=r + 2, column=1)
btn0.grid(sticky="nsew", row=r + 3, column=1)
# ====================Column2================
btncot = Button(calculator, bg="#22aa7a", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='cot',
                command=lambda: charenter('cot'))
btntan = Button(calculator, bg="#22aa7a", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='tan',
                command=lambda: charenter('tan'))
btnpi = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='π',
                command=lambda: charenter('π'))
btn9 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=9,
              command=lambda: charenter(9))
btn6 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=6,
              command=lambda: charenter(6))
btn3 = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=3,
              command=lambda: charenter(3))
btncb = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text=')',
               command=lambda: charenter(')'))

btncot.grid(sticky="nsew", row=r-3, column=2)
btntan.grid(sticky="nsew", row=r-2, column=2)
btnpi.grid(sticky="nsew", row=r-1,column=2)
btn9.grid(sticky="nsew", row=r, column=2)
btn6.grid(sticky="nsew", row=r + 1, column=2)
btn3.grid(sticky="nsew", row=r + 2, column=2)
btncb.grid(sticky="nsew", row=r + 3, column=2)
# ====================Column3================
btnpow = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='^',
                command=lambda: charenter('^'))
btnrad = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='rad',
                command=lambda: charenter('rad'))
btnpoint = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='.',
                command=lambda: charenter('.'))
btndiv = Button(calculator, bg="#fac534", activebackground="#cf7611", fg="#000", font=('Tw Cen MT', 20), text='/',
                command=lambda: charenter('/'))
btnmul = Button(calculator, bg="#fac534", activebackground="#cf7611", fg="#000", font=('Tw Cen MT', 20), text='x',
                command=lambda: charenter('x'))
btnsub = Button(calculator, bg="#fac534", activebackground="#cf7611", fg="#000", font=('Tw Cen MT', 20), text='-',
                command=lambda: charenter('-'))
btnadd = Button(calculator, bg="#fac534", activebackground="#cf7611", fg="#000", font=('Tw Cen MT', 20), text='+',
                command=lambda: charenter('+'))
btnpow.grid(sticky="nsew", row=r-3, column=3)
btnrad.grid(sticky="nsew", row=r-2, column=3)
btnpoint.grid(sticky="nsew",row=r-1,column=3)
btndiv.grid(sticky="nsew", row=r, column=3)
btnmul.grid(sticky="nsew", row=r + 1, column=3)
btnsub.grid(sticky="nsew", row=r + 2, column=3)
btnadd.grid(sticky="nsew", row=r + 3, column=3)
# ====================Column4================
btnroot = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='√',
                 command=lambda: charenter('√('))
btne = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='e',
                 command=lambda: charenter('e'))
btndeg = Button(calculator, bg="#3d3d3d", activebackground="#cf7611", fg="#fff", font=('Tw Cen MT', 20), text='°',
                command=lambda: charenter('°'))
btnallclear = Button(calculator, bg="#f52314", activebackground="#ff5d52", fg="#000", font=('Tw Cen MT', 20, 'bold'),
                     text='AC', command=allclear)
btnclear = Button(calculator, bg="#fff", activebackground="#f3ff52", fg="#000000", font=('Tw Cen MT', 20, 'bold'),
                  text='C', command=clear)
btnequal = Button(calculator, bg="#02a125", activebackground="#00d930", fg="#000", font=('Tw Cen MT', 20), text='=',
                  command=equal)

btnroot.grid(sticky="nsew", row=r-3, column=4)
btne.grid(sticky="nsew", row=r-1,column=4)
btndeg.grid(sticky="nsew", row=r-2, column=4)
btnallclear.grid(sticky="nsew", row=r, column=4)
btnclear.grid(sticky="nsew", row=r + 1                 , column=4)
btnequal.grid(sticky="nsew", row=r + 2, column=4, rowspan=2)

# --------------------------------Functions-End---------------------------------------------
for i in range(0, calculator.grid_size()[0]):
    calculator.columnconfigure(i, weight=1)
for i in range(0, calculator.grid_size()[1]):
    calculator.rowconfigure(i, weight=1)
no_of_col = int(calculator.grid_size()[1])
# --------------------------------Entry---------------------------------------------
entry = Entry(calculator, justify="right", font=("Tw Cen MT", 25), bg="#757575",fg="#222")
entry.grid(row=0, column=0, columnspan=no_of_col, sticky="nsew")
btnclose=Button(calculator,text="Close",command=calculator.destroy)
btnclose.grid(row=100,column=0,columnspan=calculator.grid_size()[0],sticky="nsew")
btnclose.config(font=("Tw Cen MT",20),fg="#fff",bg="#3d3d3d",relief=RAISED,bd=3,width=30)
calculator.mainloop()
