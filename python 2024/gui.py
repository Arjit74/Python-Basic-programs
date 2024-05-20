# GUI ==>>> GRAPHICAL USER INTERFACE
# import tkinter as tk
from tkinter import *

root = Tk()
root.geometry('2000x1000')
root.title('first app by Arjit')
root.minsize(1000 , 500)
def my_fun1():
    lb.config(text=lb.cget('text')+1)
def my_fun2():
    lb.config(text=lb.cget('text')-1)
  
lb = Label(root , text=0)
lb.pack()
bt1 = Button(root , text=' + ' , command=my_fun1)
bt1.pack()
bt2 = Button(root , text=' - ' , command=my_fun2)
bt2.pack()

root.mainloop()