import tkinter
from io import BytesIO

import customtkinter
import pytube
from pytube import YouTube

from PIL import Image, ImageTk
import requests

SAVE_PATH = '/home/collyne/Downloads'


def startDownload():
    try:
        showText.configure(text="")
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        video.download(SAVE_PATH)
        setThumbnail(yt_object.thumbnail_url)
        # Finished downloading label
        showText.configure(text="Download Complete", text_color="green")

    except pytube.exceptions.RegexMatchError:

        showText.configure(text="Invalid YouTube link!", text_color="red")

    except pytube.exceptions.VideoUnavailable:

        showText.configure(text="Video is unavailable!", text_color="red")

    except Exception as e:

        showText.configure(text="An error occurred: " + str(e), text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_downloaded = round(bytes_downloaded / total_size * 100, 2)
    per = str(int(percentage_downloaded))

    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #     update progress bar
    progressBar.set(float(percentage_downloaded / 100))


def setThumbnail(thumbnail_url):
    try:
        response = requests.get(thumbnail_url)
        if response.status_code == 200:
            # Convert the response content to bytes
            image_data = BytesIO(response.content)
            # Open the image using PIL/Pillow
            pil_image = Image.open(image_data)
            # Convert the PIL image to Tkinter PhotoImage
            tk_image = ImageTk.PhotoImage(pil_image)
            # Display the image in a Tkinter label
            thumbnail_label = customtkinter.CTkLabel(image=tk_image)
            thumbnail_label.pack()
            # Keep a reference to the image to prevent it from being garbage collected
            thumbnail_label.image = tk_image
        else:
            # Error downloading image
            showText.configure(text="Failed to download thumbnail!", text_color="red")
    except Exception as e:
        # Other exceptions
        showText.configure(text="An error occurred: " + str(e), text_color="red")


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding ui elements
title = customtkinter.CTkLabel(app, text="Enter youtube link")
title.pack(padx=5, pady=5)

# link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
button_download = customtkinter.CTkButton(app, text="Download", command=startDownload)
button_download.pack(padx=5, pady=5)

# Show text output

showText = customtkinter.CTkLabel(app, text="")
showText.pack(padx=5, pady=5)

# Progress bar
pPercentage = customtkinter.CTkLabel(app, text="0 %")
pPercentage.pack(padx=5, pady=5)

progressBar = customtkinter.CTkProgressBar(app, width=350)
progressBar.set(0)
progressBar.pack(padx=5, pady=5)

# run app
app.mainloop()
