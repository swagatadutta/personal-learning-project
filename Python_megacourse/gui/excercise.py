from tkinter import *

window=Tk()

def kg_converter():
    kg=float(e1_val.get())
    grams=kg*1000.0
    pounds=kg*2.20462
    ounces=kg*35.274

    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

l1=Label(window, text="Kg")
l1.grid(row=0, column=0)

l2=Label(window, text="Grams")
l2.grid(row=1, column=0)

l3=Label(window, text="Pounds")
l3.grid(row=1, column=1)

l4=Label(window, text="Ounces")
l4.grid(row=1, column=2)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0, column=1)

b1=Button(window,text="Convert", command=kg_converter)
b1.grid(row=0,column=2)

t1=Text(window, height=1, width=20)
t1.grid(row=2, column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=2, column=1)

t3=Text(window, height=1, width=20)
t3.grid(row=2, column=2)

window.mainloop()
