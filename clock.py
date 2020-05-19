from tkinter import *
from tkinter.ttk import *
from time import strftime
from random import randint

root = Tk()
root.title('Clock')


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)



bg = "%06x" % randint(0, 0xFFFFFF)
fg = "%06x" % randint(0, 0xFFFFFF)

lbl = Label(root, font=('calibri', 40, 'bold'),background='#'+bg, foreground='#'+fg)
lbl.pack(anchor='center')

time()
mainloop()