import io
import os
import platform
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen

import customtkinter
import pytube
import requests
from CTkMenuBar import *
from pytube import YouTube

from menu_spawn import *


import sqlite3 as sq

# conn = sq.connect(':memory:')
conn = sq.connect("info.db")
exc = conn.cursor()

SAVE_PATH = "/home/collyne/Downloads"
YT_OBJECT = None
VIDEO_FOUND = None
THEME = exc.execute("SELECT current_theme from theme").fetchone()[0]


# https://youtu.be/c4l8e7pJCsA?si=ZwVzSDLLbwSu5QYR

import sys


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# noinspection PyUnresolvedReferences
# method to update the progress bar basing on download progress
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_downloaded = round(bytes_downloaded / total_size * 100, 2)
    per = str(int(percentage_downloaded))

    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Check if the Tkinter application is still running
    if progressBar.winfo_exists():
        progressBar.set(float(percentage_downloaded / 100))


def showSearchingText():
    text.configure(text="searching", text_color="black", bg_color="yellow")
    text.place(x=0, y=30)
    # Create a new thread for the download process
    if search_thread.is_alive():
        userResponse = messagebox.askyesno(
            "Warning",
            "A search is still in progress, are you sure you want to cancel",
        )
        if userResponse:
            search_thread.start()
    else:
        search_thread.start()


# method to search for video existence on YouTube
def searchVideo():
    # Hide the download button and the progress bar
    button_download.pack_forget()
    progressBar.pack_forget()

    # Clear the progress bar
    progressBar.pack_forget()
    pPercentage.pack_forget()
    button_frame.pack_forget()

    # Set the progress bar to zero
    progressBar.set(0)
    pPercentage.configure(text="0 %")
    pPercentage.pack_forget()
    button_frame.pack_forget()

    # Set the progress bar to zero
    progressBar.set(0)

    # Remove the photo from the details frame
    for widget in details_frame.winfo_children():
        widget.pack_forget()

    # Remove the video title
    video_title.configure(text="")

    details_frame.pack_forget()

    # Update the window size to fit the new layout

    try:
        # Send a request to google.com to check for an internet connection
        requests.get("https://google.com", timeout=5)

        # If the request succeeds, continue with YouTube search

        global YT_OBJECT, VIDEO_FOUND
        try:
            yt_link = link.get()
            YT_OBJECT = YouTube(yt_link, on_progress_callback=on_progress)
            VIDEO_FOUND = YT_OBJECT.streams.get_highest_resolution()

            my_option.pack(side="left", padx=5, pady=5)

            # hide searching
            text.place_forget()

            displayImage_and_details()

            # display download button
            button_frame.pack(pady=10)  # embedd frame
            button_download.pack(side="left", padx=5)

        except pytube.exceptions.RegexMatchError:
            text.configure(
                text="Invalid YouTube link!", text_color="white", bg_color="red"
            )
            text.place(x=0, y=30)

        except pytube.exceptions.VideoUnavailable:
            text.configure(
                text="Video is unavailable!", text_color="white", bg_color="red"
            )
            text.place(x=0, y=30)

        except Exception as e:
            text.configure(
                text="An error occurred: " + str(e), text_color="white", bg_color="red"
            )
            text.place(x=0, y=30)

            # display error for a poor connection
    except (requests.ConnectionError, requests.Timeout) as exception:
        # If the request fails, show an error message and return
        text.configure(
            text="No internet connection!", text_color="white", bg_color="red"
        )
        text.place(x=0, y=30)
        return


# method to start download on click of download button


def download_thread():
    try:
        if my_option.get() == "mp3":
            audio_stream = YT_OBJECT.streams.filter(only_audio=True).first()
            if audio_stream:
                text.configure(
                    text="Downloading ....", text_color="green", bg_color="white"
                )
                text.place(x=0, y=30)
                output_file = audio_stream.download(output_path=SAVE_PATH)
                base, ext = os.path.splitext(output_file)
                new_file = base + ".mp3"
                os.rename(output_file, new_file)

                # show message
                text.configure(
                    text="Audio download Complete", text_color="white", bg_color="green"
                )
                text.place(x=0, y=30)

                # remove progress bar
                pPercentage.pack_forget()
                progressBar.pack_forget()
                return
            else:
                # show message
                text.configure(
                    text="No audio stream found!", text_color="white", bg_color="red"
                )
                text.place(x=0, y=30)
                return

        elif my_option.get() == "mp4":

            text.configure(
                text="Downloading ....", text_color="green", bg_color="white"
            )
            text.place(x=0, y=30)

            VIDEO_FOUND.download(SAVE_PATH)
            # show message
            text.configure(
                text="Video download Complete", text_color="white", bg_color="green"
            )
            text.place(x=0, y=30)

            # remove progress bar
            pPercentage.pack_forget()
            progressBar.pack_forget()
            return

    except pytube.exceptions.VideoUnavailable:
        # show message
        text.configure(text="Video is unavailable!", text_color="white", bg_color="red")
        text.place(x=0, y=30)
    except pytube.exceptions.RegexMatchError:

        # show message
        text.configure(text="Invalid Youtube link", text_color="white", bg_color="red")
        text.place(x=0, y=30)

    except Exception as e:
        # show message
        text.configure(text="An error occurred !", text_color="white", bg_color="red")
        text.place(x=0, y=30)
        print(e)

        pPercentage.pack(padx=5, pady=5)
        progressBar.pack(padx=5, pady=5)


def startDownload():
    # Create a new thread for the download process
    if download_thread_obj.is_alive():
        userResponse = messagebox.askyesno(
            "Warning",
            "A download is still in progress, are you sure you want to cancel",
        )
        if userResponse:
            download_thread_obj.start()
    else:
        download_thread_obj.start()

    # Update GUI elements (if needed)
    pPercentage.pack(padx=5, pady=5)
    progressBar.pack(padx=5, pady=5)


def clearEntry():
    url_var.set("")
    text.place_forget()

    # Hide the download button and the progress bar
    button_download.pack_forget()
    progressBar.pack_forget()
    pPercentage.pack_forget()
    button_frame.pack_forget()

    # Set the progress bar to zero
    progressBar.set(0)

    # Remove the photo from the details frame
    for widget in details_frame.winfo_children():
        widget.pack_forget()

    # Remove the video title
    video_title.configure(text="")

    details_frame.pack_forget()


def displayImage_and_details():
    details_frame.pack(pady=10)
    # Display thumbnail image
    imageUrl = YT_OBJECT.thumbnail_url
    u = urlopen(imageUrl)
    raw_data = u.read()
    u.close()

    # Open image using PIL
    image = Image.open(io.BytesIO(raw_data))

    # Resize image
    resized_image = image.resize((200, 150))  # Adjust the size as needed

    # Convert image to PhotoImage
    photo = ImageTk.PhotoImage(resized_image)

    # Create label with the resized image
    label = tk.Label(details_frame, image=photo)
    label.image = photo
    label.pack(side="left")  # Display image on the left side

    # Display video title
    video_title.configure(text=YT_OBJECT.title)
    # Display video title
    video_title.configure(
        text=YT_OBJECT.title, font=("Helvetica", 18, "bold"), wraplength=200
    )  # Increase font size
    video_title.pack(
        side="right", padx=5, pady=(20, 10)
    )  # Display title on the right side with padding


# menu commands


def opendownloadsFolder():
    system = platform.system()
    if system == "Windows":
        # Replace <Username> with your actual username
        subprocess.Popen(f'explorer /select, "{SAVE_PATH}"')
    elif system == "Darwin":  # macOS
        # macOS typically opens the Downloads folder with this command
        subprocess.Popen(["open", SAVE_PATH])
    elif system == "Linux":
        # Linux typically opens the Downloads folder with this command
        subprocess.Popen(["xdg-open", SAVE_PATH])
    else:
        print("Unsupported operating system.")


def closeProgram():
    if search_thread.is_alive() or download_thread_obj.is_alive():
        userResponse = messagebox.askyesno(
            "Warning",
            "Tube fetch is currently running some processes, are you sure you want to cancel",
        )
        if userResponse:
            exit()
    else:
        exit()


def Menu():
    menu = CTkMenuBar(app)
    button_1 = menu.add_cascade("File")
    button_3 = menu.add_cascade("Settings")
    button_4 = menu.add_cascade("Help")

    dropdown1 = CustomDropdownMenu(widget=button_1)
    dropdown1.add_option(option="Open downloads", command=opendownloadsFolder)
    # dropdown1.add_option(option="Quit", command=closeProgram)
    dropdown1.add_option(option="Quit", command=restart_program)

    dropdown1.add_separator()

    dropdown3 = CustomDropdownMenu(widget=button_3)
    dropdown3.add_option(option="Preferences", command=lambda: Preferences())

    dropdown4 = CustomDropdownMenu(widget=button_4)
    dropdown4.add_option(option="Check for updates")
    dropdown4.add_option(option="About", command=lambda: About())


# initialise elements

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme(f"theme/{THEME}.json")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.resizable(0, 0)
app.title("Tube Fetch")


iconpath = ImageTk.PhotoImage(file=os.path.join("assets", "logo.png"))
app.after(300, lambda: app.iconphoto(False, iconpath))

Menu()


# Adding ui elements

# Create a Frame to contain the buttons

textEntry_frame = customtkinter.CTkFrame(app)
textEntry_frame.pack(pady=(80, 10))  # Adjust pady as needed

# link
url_var = tk.StringVar()
link = customtkinter.CTkEntry(
    textEntry_frame, width=350, height=40, textvariable=url_var
)

# First Download Button
clearButton = customtkinter.CTkButton(
    textEntry_frame, width=50, height=40, text="clear", command=clearEntry
)

# First Download Button
searchButton = customtkinter.CTkButton(
    textEntry_frame, height=40, text="search", command=showSearchingText
)

# Create a Frame to contain the buttons
button_frame = customtkinter.CTkFrame(app)


# Second Download Button
button_download = customtkinter.CTkButton(
    button_frame, text="Download", command=startDownload
)

file_formats = ["mp4", "mp3"]

# create option menu
my_option = customtkinter.CTkOptionMenu(button_frame, values=file_formats)


# Show text output

showError_Success = customtkinter.CTkLabel(app, text="")
showError_Success.pack(padx=5, pady=5)
#
# Progress bar
pPercentage = customtkinter.CTkLabel(app, text="0 %")

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=350, height=5)
progressBar.set(0)


# Adjust the width of the details frame based on the width of other widgets
width = (
    link.winfo_reqwidth()
    + clearButton.winfo_reqwidth()
    + searchButton.winfo_reqwidth()
    + 20
)

# details frame
details_frame = customtkinter.CTkFrame(app, width=width)

# image frame
video_title = customtkinter.CTkLabel(details_frame, text="")


searching_text = customtkinter.CTkLabel(
    app, text="Searching......", text_color="yellow"
)
text = customtkinter.CTkLabel(
    app, text="searching", text_color="black", width=720, bg_color="yellow"
)


# initialise threads
download_thread_obj = threading.Thread(target=download_thread)
search_thread = threading.Thread(target=searchVideo)


# run app
def startMain():
    link.pack(side="left", padx=5)
    clearButton.pack(side="left", padx=5)
    searchButton.pack(side="left", padx=5)
    app.mainloop()
