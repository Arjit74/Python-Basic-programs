# import tkinter as tk

# root = tk.Tk()
# root.configure(bg='skyblue')
# def action1():
#     data = lb.cget('text')
#     data = int(data) + 1
#     lb.configure(text=str(data))
#     print(txt.get(1.0, tk.END))
# def action2():
#     data = lb.cget('text')
#     data = int(data) - 1
#     lb.config(text=str(data))
# lb = tk.Label(root, text='0', bg='red')
# lb.pack()

# txt = tk.Text(root)
# txt.pack()
# bt1 = tk.Button(root, text='  INC  ', command=action1)
# bt1.pack()
# bt2 = tk.Button(root, text='  DEC   ', command=action2)
# bt2.pack()
# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.geometry('500x300')
root.title('increment and decrement')

def action1():
    val = lb.cget('text')
    conval = int(val) + 1
    lb.config(text = str(conval))
def action2():
    val = lb.cget('text')
    val = int(val) - 1
    lb.config(text = val)

lb = tk.Label(root,text ='0',fg = 'yellow',bg = 'red')
lb.pack(fill = "both" ,ipadx = 15 , ipady = 10 , padx = 20 )
bt1 = tk.Button(root,text = ' Increment ' , command = action1 , fg = 'white' , bg = 'red' )
bt2 = tk.Button(root, text = ' Decrement ' , command = action2,  fg = 'white' , bg = 'red')
bt1.pack(side = 'bottom',pady = 20)
bt2.pack(side = 'bottom')

root.mainloop()