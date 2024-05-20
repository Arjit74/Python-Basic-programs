#BMI
import tkinter as tk

class BMI:
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow
        mainwindow.geometery('400x300')

        self.lb1 = tk.Label(self.mainwindow,text = 'BMI Calculator')
        self.lb1.grid(row=0,column=4)
        
        self.lb2 = tk.Label(self.mainwindow,text = 'Height(m)')
        self.lb2.grid(row=2,column=5)

        self.height = tk.Entry(self.mainwindow)
        self.height.grid(row=3,column=5) 

        self.lb3 = tk.Label(self.mainwindow,text='Weight(kgs)')
        self.lb3.grid(row=2,column = 6)

        self.weight = tk.Entry(self.mainwindow)
        self.weight.grid(row=4,column=5)


        self.bt1 = tk.Button(self.mainwindow,text='Calculate',command=action)

        self.output = tk.Lable(self.mainwindow,text ='')
        self.output.grid(row=8,column=5)
    
        def action(self):
            val1 = float(self.height.get())
            val2 = float(self.weight.get())
            ans = val2/(val1 **2)
            self.output.config(f"Your BMI is {ans} ")
     
        root = tk.Tk()
        self.root.mainloop()