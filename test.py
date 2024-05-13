import tkinter as tk


def hide_item():
    label.pack_forget()  # Hide the label


def show_item():
    label.pack()  # Display the label


root = tk.Tk()

label = tk.Label(root, text="Hello, World!")
label.pack()

hide_button = tk.Button(root, text="Hide", command=hide_item)
hide_button.pack()

show_button = tk.Button(root, text="Show", command=show_item)
show_button.pack()

root.mainloop()
