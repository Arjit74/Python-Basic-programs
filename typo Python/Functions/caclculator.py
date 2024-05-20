import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
root.geometry('1600x900')
class image:
    def _init_(self,mainwindow,dir):
        self.x = 1
        self.mainwindow = mainwindow
        self.dir = dir
        self.img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Asus\\Downloads\\CARS\\1.png").resize((1300, 700)))

        self.panel = tk.Label(mainwindow, image = self.img)
        self.panel.grid(row=0, column=0, columnspan=2) 
        self.panel.image = self.img  
        self.bt1 = tk.Button(self.mainwindow,text='Previous',command=self.previous)
        self.bt1.grid(row=4,column=0)
        self.bt2 = tk.Button(self.mainwindow,text='Next',command=self.next)
        self.bt2.grid(row=4,column=1)
        
    def previous(self):
        if self.x>1:
            self.x-=1
        image = Image.open(self.dir+'\\'+str(self.x)+'.png')
        resize_image = image.resize((1300, 700))

        self.photo = ImageTk.PhotoImage(resize_image)
        self.panel.config(image = self.photo)
        
    
    def next(self):
        if self.x<10:
            self.x+=1
        image= Image.open(self.dir+'\\'+str(self.x)+'.png')
        resize_image = image.resize((1300, 700))
        self.photo = ImageTk.PhotoImage(resize_image)
        self.panel.config(image = self.photo)
        

image(root,"C:\\Users\\Asus\\Downloads\\CARS")
root.mainloop()