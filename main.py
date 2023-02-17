from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("What time is it? It's: ")


def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font= ('calibri', 80), background = 'orange', foreground = 'violet')
label.pack(anchor = 'center')

time()

root.mainloop()