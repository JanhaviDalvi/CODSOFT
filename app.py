#Task 2 : Calculator
from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry('350x400')
root.minsize(350,100)
root.maxsize(500,600)

T = Text(root, height = 2, width = 50)
T.pack(padx= 10, pady=20)
root.mainloop() 