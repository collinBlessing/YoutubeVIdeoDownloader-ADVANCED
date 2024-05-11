from tkinter import *
from main import app
menu = Menu(app)
app.config(menu=menu)

def our_command():
    pass

# create a menu item
file_menu = Menu(menu)
menu.add_cascade(Label="File", menu=menu)
file_menu.add_cascade(Label="New ...", command=our_command)