import customtkinter as ctk
from PIL import Image, ImageTk
import os
from tkinter.filedialog import askdirectory
import webbrowser
import sqlite3 as sq
from utils import restart_program

conn = sq.connect("info.db")
exc = conn.cursor()


def Preferences():
    def saveChanges():
        theme_changed = False
        # save theme
        CURRENT_THEME = exc.execute("SELECT current_theme from theme").fetchone()[0]
        NEW_THEME = themeOptions.get()

        CURRENT_SAVE_PATH = exc.execute("SELECT download_path from path").fetchone()[0]
        NEW_SAVE_PATH = download_folder_location.cget("text")

        # set state from the check
        CURRENT_AUTO_SAVE_STATE = exc.execute(
            "SELECT auto_download from path"
        ).fetchone()[0]

        # set state from the check
        if automatic_download.get():
            NEW_AUTO_SAVE_STATE = "true"
        else:
            NEW_AUTO_SAVE_STATE = "false"

        print(CURRENT_AUTO_SAVE_STATE)
        print(NEW_AUTO_SAVE_STATE)

        if (
            NEW_THEME != CURRENT_THEME
            or CURRENT_SAVE_PATH != NEW_SAVE_PATH
            or CURRENT_AUTO_SAVE_STATE != NEW_AUTO_SAVE_STATE
        ):

            if NEW_THEME != CURRENT_THEME:
                exc.execute(
                    "UPDATE theme SET current_theme = ? WHERE ID = 1", (NEW_THEME,)
                )
                theme_changed = True

            if CURRENT_SAVE_PATH != NEW_SAVE_PATH:
                exc.execute(
                    "UPDATE path SET download_path = ? WHERE ID = 1", (NEW_SAVE_PATH,)
                )

            if CURRENT_AUTO_SAVE_STATE != NEW_AUTO_SAVE_STATE:
                exc.execute(
                    "UPDATE path SET auto_download = ? WHERE ID = 1",
                    (NEW_AUTO_SAVE_STATE,),
                )



            conn.commit()

            text.configure(
                text="Changes saved successfully", bg_color="green", text_color="white"
            )
            text.place(x=0, y=0)

            if theme_changed:
                restart_program()
        else:
            text.configure(
                text="No changes to make", bg_color="yellow", text_color="black"
            )
            text.place(x=0, y=0)

        #

    def chooseSelection():
        new_path = "{}".format(askdirectory(title="Choose directrory", mustexist=True))
        download_folder_location.configure(text=new_path)

    preferences_window = ctk.CTk()
    preferences_window.geometry("600x320")
    preferences_window.title("Preferences")
    iconpath = ImageTk.PhotoImage(file=os.path.join("assets", "logo.png"))
    preferences_window.after(300, lambda: preferences_window.iconphoto(False, iconpath))
    preferences_window.resizable(0, 0)

    # unsaved changes
    text = ctk.CTkLabel(
        preferences_window,
        text_color="white",
        width=600,
        bg_color="green",
    )

    downloadFolder = ctk.CTkFrame(preferences_window)
    # Labels
    download_folder_label = ctk.CTkLabel(downloadFolder, text="Download Folder:")
    download_folder_label.pack(side="left", padx=10, pady=10)
    # Labels
    download_folder_location = ctk.CTkLabel(
        downloadFolder,
        text="/home/collyne/downloads",
        wraplength=150,
        text_color="green",
    )

    download_folder_location.pack(side="left", padx=10, pady=10)

    # Button
    download_folder_Button = ctk.CTkButton(
        downloadFolder, text="change", command=chooseSelection
    )
    download_folder_Button.pack(side="left", padx=10, pady=10)

    downloadFolder.pack(padx=10, pady=(50, 10))

    # theme text
    themeFrame = ctk.CTkFrame(preferences_window)
    themeText = ctk.CTkLabel(themeFrame, text="Choose Theme", wraplength=150)

    themeText.pack(side="left", padx=(10, 60), pady=10)

    # TODO: fix error on about page on the icon
    # options

    themes = ["marsh", "metal", "pink", "red", "violet", "yellow"]
    themeOptions = ctk.CTkOptionMenu(themeFrame, values=themes)

    CURRENT_THEME = exc.execute("SELECT current_theme from theme").fetchone()[0]
    themeOptions.set(CURRENT_THEME)

    themeOptions.pack(side="left", padx=10, pady=10)
    themeFrame.pack(padx=10, pady=10)

    # Automatically download files
    automatic_download = ctk.CTkCheckBox(
        preferences_window, text="start downloading files automatically"
    )
    automatic_download.pack(padx=(10, 60), pady=10)

    # save button
    saveButton = ctk.CTkButton(preferences_window, text="Save", command=saveChanges)
    saveButton.pack(padx=10, pady=10)

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
        about_window, height=5, text="Visit portfolio", command=visitPortfolio
    )
    button_link.pack(padx=10, pady=10)

    about_window.mainloop()


Preferences()
