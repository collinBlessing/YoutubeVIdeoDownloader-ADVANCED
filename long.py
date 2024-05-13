import tkinter
import customtkinter




frame  = customtkinter.CTk()
frame.geometry("720x250")
frame.resizable(0,0)

text = customtkinter.CTkLabel(frame , text="searching", text_color="black", width=720, bg_color="yellow")
text.pack()




frame.mainloop()