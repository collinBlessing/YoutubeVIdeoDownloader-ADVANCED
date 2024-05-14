import customtkinter as ctk
from PIL import Image, ImageTk
import os
from tkinter.filedialog import askdirectory
import webbrowser


def Preferences():
    def chooseSelection():
        new_path = '{}'.format(askdirectory(
            title='Choose directrory', mustexist=True))
        print(new_path)

    preferences_window = ctk.CTk()
    preferences_window.geometry("420x320")
    preferences_window.title("Preferences")
    iconpath = ImageTk.PhotoImage(file=os.path.join("assets", "logo.png"))
    preferences_window.after(
        300, lambda: preferences_window.iconphoto(False, iconpath))
    preferences_window.resizable(0, 0)

    # Labels
    download_folder_label = ctk.CTkLabel(
        preferences_window, text="Download Folder:")
    download_folder_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    # Labels
    download_folder_location = ctk.CTkLabel(
        preferences_window, text="/home/collyne/downloads", wraplength=150, text_color="yellow")

    download_folder_location.grid(
        row=0, column=1, padx=45, pady=10, sticky="w")

    # Button
    download_folder_Button = ctk.CTkButton(
        preferences_window, text="...", width=10, command=chooseSelection)
    download_folder_Button.grid(row=0, column=2, padx=20, pady=10, sticky="w")

    preferences_window.mainloop()


def About():
    about_window = ctk.CTk()
    about_window.geometry("420x320")
    about_window.title("About")
    iconpath = ImageTk.PhotoImage(file=os.path.join("assets", "logo.png"))
    about_window.after(300, lambda: about_window.iconphoto(False, iconpath))
    about_window.resizable(0, 0)

    # Labels
    text_label = ctk.CTkLabel(
        about_window,
        wraplength=300,
        text="Tube Fetch is developed by Nahurira Collin Blessing, a proficient Full Stack Developer known for crafting intuitive and efficient software solutions. With Collin's expertise in both frontend and backend development, Tube Fetch offers users a seamless experience for downloading YouTube content in MP3 and MP4 formats. Nahurira Colin Blessing's dedication to delivering high-quality applications ensures that Tube Fetch meets the needs of users seeking a reliable and user-friendly YouTube downloader.",
    )
    text_label.pack(padx=0, pady=40)

    def visitPortfolio():
        webbrowser.open(link_text)

    link_text = "http://www.nahuriracollinblessing.com"
    button_link = ctk.CTkButton(
        about_window, text='Visit portfolio', command=visitPortfolio)
    button_link.pack(padx=10, pady=10)

    about_window.mainloop()


# About()
