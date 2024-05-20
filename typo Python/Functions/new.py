import tkinter as tk
from PIL import ImageTk, Image

class ImageViewer:
    def __init__(self, master, images):
        self.master = master
        self.images = images
        self.index = 0

        # Load and display the initial image
        self.image = Image.open(self.images[self.index])
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(master, image=self.photo)
        self.label.pack()

        # Create 'previous' button
        prev_button = tk.Button(master, text='Previous', command=self.prev_image)
        prev_button.pack(side='left', padx=10, pady=10)

        # Create 'next' button
        next_button = tk.Button(master, text='Next', command=self.next_image)
        next_button.pack(side='right', padx=10, pady=10)

        # Set minimum size for the main window
        master.minsize(400, 300)  # Set your desired minimum size here

    def prev_image(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.images) - 1
        self.update_image()

    def next_image(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.update_image()

    def update_image(self):
        self.image = Image.open(self.images[self.index])
        self.photo = ImageTk.PhotoImage(self.image)
        self.label.config(image=self.photo)
        self.label.image = self.photo

if __name__ == "__main__":
    root = tk.Tk()
    images = [
        r'C:\Users\ARJIT SHARMA\Downloads\IMG-20240215-WA0012.jpg',
        r'C:\Users\ARJIT SHARMA\Downloads\Downloads\girl.jpg',
        r'C:\Users\ARJIT SHARMA\Downloads\Downloads\sundar kanya.jpg',
    ] 
    viewer = ImageViewer(root, images)
    root.mainloop()

