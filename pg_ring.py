import customtkinter
import awesometkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

HEIGHT = 250
WIDTH = 370

app = customtkinter.CTk()
# app.title("Circular Progress Bar")
app.geometry((f"{WIDTH}x{HEIGHT}"))


app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

bg_progress = None
if app.cget("background") == 'gray14':
    bg_progress = "#242424"
else:
    bg_progress = "#EBEBEB"


indicatorBar = awesometkinter.RadialProgressbar(
    app, fg="green", parent_bg=bg_progress, size=(50, 50)
)

indicatorBar.pack()

indicatorBar.start()




# Print the color code

app.mainloop()
