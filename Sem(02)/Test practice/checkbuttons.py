# import tkinter as tk

# root = tk.Tk()
# radio_button1 = tk.Radiobutton(root, text="Option 1")
# radio_button2 = tk.Checkbutton(root, text="Option 2")
# radio_button1.pack()
# radio_button2.pack()

# root.mainloop()

import tkinter as tk

def deselect_all():
    selected_option.set("")  # Set the associated variable to an empty string

root = tk.Tk()
selected_option = tk.StringVar()  # Create a StringVar to hold the selected option
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1")
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2")
radio_button1.pack()
radio_button2.pack()

clear_button = tk.Button(root, text="Clear Selection", command=deselect_all)
clear_button.pack()

root.mainloop()
