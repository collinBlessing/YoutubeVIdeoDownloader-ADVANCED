from tkinter import *
from PIL import ImageTk, Image
import time
import os
w = Tk()

# Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
w.geometry(
    "%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate)
)
w.overrideredirect(1)  # for hiding titlebar


# new window to open
def callMainWindow():
    import main

    main.startMain()


frame = Frame(w, width=427, height=250, bg="#000")
frame.place(x=0, y=0)
label1 = Label(w, text="Tube Fetch", fg="white", bg="#000")  # decorate it
label1.configure(
    font=("Game Of Squids", 24, "bold")
)  # You need to install this font in your PC or try another one
label1.place(x=110, y=70)

# New code for adding the "Developed by" label
developed_by_text = "Developed by Nahurira Collin Blessing"
developed_by_label = Label(w, text=developed_by_text, fg="white", bg="#000")
developed_by_label.configure(font=("Calibri", 10, "bold"))
developed_by_label.place(x=75, y=200)

# making animation
image_a = ImageTk.PhotoImage(file=os.path.join("assets", "c1.png"))
image_b = ImageTk.PhotoImage(file=os.path.join("assets", "c2.png"))


def animate():
    for i in range(1):  # 5 loops
        l1 = Label(w, image=image_a, border=0, relief=SUNKEN)
        l1.place(x=180, y=145)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l2.place(x=200, y=145)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l3.place(x=220, y=145)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l4.place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l1.place(x=180, y=145)
        l2 = Label(w, image=image_a, border=0, relief=SUNKEN)
        l2.place(x=200, y=145)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l3.place(x=220, y=145)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l4.place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l1.place(x=180, y=145)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l2.place(x=200, y=145)
        l3 = Label(w, image=image_a, border=0, relief=SUNKEN)
        l3.place(x=220, y=145)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l4.place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l1.place(x=180, y=145)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l2.place(x=200, y=145)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN)
        l3.place(x=220, y=145)
        l4 = Label(w, image=image_a, border=0, relief=SUNKEN)
        l4.place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

    w.destroy()
    callMainWindow()


# Schedule the animation to run before opening the main window
w.after(1000, animate)  # Wait 2 seconds before starting the animation

w.mainloop()
