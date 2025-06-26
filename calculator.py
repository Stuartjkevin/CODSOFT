
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x300")

Number1 = IntVar()
Number2 = IntVar()

l1 = Label(window, text='CALCULATOR')
l1.place(x=200, y=20)

l2 = Label(window, text='Number1')
l2.place(x=50, y=100)
t1 = Entry(window, textvariable=Number1)
t1.place(x=150, y=100)

l3 = Label(window, text='Number2')
l3.place(x=50, y=150)
t2 = Entry(window, textvariable=Number2)
t2.place(x=150, y=150)

def add():
    result = Number1.get() + Number2.get()
    output.config(text='RESULT = {}'.format(result))

def sub():
    result = Number1.get() - Number2.get()
    output.config(text='RESULT = {}'.format(result))

def mul():
    result = Number1.get() * Number2.get()
    output.config(text='RESULT = {}'.format(result))

def div():
    if Number2.get() == 0:
        messagebox.showerror("Error", "Division by zero")
    else:
        result = Number1.get() / Number2.get()
        output.config(text='RESULT = {:.2f}'.format(result))

b1 = Button(window, text='+', command=add)
b1.place(x=50, y=200)

b2 = Button(window, text='-', command=sub)
b2.place(x=100, y=200)

b3 = Button(window, text='*', command=mul)
b3.place(x=150, y=200)

b4 = Button(window, text='/', command=div)
b4.place(x=200, y=200)

output = Label(window, text='RESULT = ')
output.place(x=150, y=250)

window.mainloop()