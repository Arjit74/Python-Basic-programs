import tkinter as tk
class Todo:
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow
        mainwindow.geometry('400 x 300')

        self.entry = tk.Entry(mainwindow)
        self.entry.grid(row=0, column=0)

        self.bt_add = tk.Button(self.mainwindow,text='Add Item', command=add_item)
        self.bt_add.grid(row=0, column=1)

        self.list_box = tk.Listbox(self.mainwindow, width=65)
        self.list_box.grid(row=1,columnspan=2)

        
        self.bt_delete = tk.Button(self.mainwindow, text='Delete Item', command=del_item)
        self.bt_delete.grid(row=2,column=0)

        bt_delete_all = tk.Button(self.mainwindow, text='Delete all Items', command=del_all_item)
        bt_delete_all.grid(row=2,column=1)

        def add_item(self):
            self.data = self.entry.get()
            self.entry.delete(0, tk.END)
            self.list_box.insert(tk.END,self.data)

        def del_item(self):
            self.select_index = self.list_box.curselection()
            self.list_box.delete(self.select_index)

        def del_all_item(self):
            self.list_box.delete(0, tk.END)

        self.root = tk.Tk()
        self.root.title('To do list')
        self.root.mainloop()