import tkinter
import customtkinter




frame  = customtkinter.CTk()
frame.geometry("720x250")
frame.resizable(0,0)



def showPopup():
    dialog = customtkinter.CTk
    dialog.pack()



text = customtkinter.CTkButton(frame , text="searching", command=showPopup)
text.pack()




frame.mainloop()