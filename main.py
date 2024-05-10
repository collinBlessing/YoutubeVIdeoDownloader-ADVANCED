import tkinter
import customtkinter
import pytube
import requests
from pytube import YouTube
import threading

SAVE_PATH = "/home/collyne/Downloads"
YT_OBJECT = None
VIDEO_FOUND = None

# https://youtu.be/c4l8e7pJCsA?si=ZwVzSDLLbwSu5QYR


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


# noinspection PyUnusedLocal
# method to search for video existence on youtube
def searchVideo():
    # Hide the download button and the progress bar
    button_download.pack_forget()
    progressBar.pack_forget()
    pPercentage.pack_forget()
    button_frame.pack_forget()

    # Set the progress bar to zero
    progressBar.set(0)
    try:
        # Send a request to google.com to check for an internet connection
        requests.get("http://google.com", timeout=5)

        # If the request succeeds, continue with youtube search

        global YT_OBJECT, VIDEO_FOUND
        try:
            showError_Success.configure(text="")
            yt_link = link.get()
            YT_OBJECT = YouTube(yt_link, on_progress_callback=on_progress)
            VIDEO_FOUND = YT_OBJECT.streams.get_highest_resolution()

            showError_Success.configure(text="Video found", text_color="yellow")

            # display download button
            button_frame.pack(pady=10)  # embedd frame
            button_download.pack(side="left", padx=5)

            # show details here
            print(YT_OBJECT.thumbnail_url)

        except pytube.exceptions.RegexMatchError:
            showError_Success.configure(text="Invalid YouTube link!", text_color="red")

        except pytube.exceptions.VideoUnavailable:
            showError_Success.configure(text="Video is unavailable!", text_color="red")

        except Exception as e:
            showError_Success.configure(
                text="An error occurred: " + str(e), text_color="red"
            )

            # display error for a poor connection
    except (requests.ConnectionError, requests.Timeout) as exception:
        # If the request fails, show an error message and return
        showError_Success.configure(text="No internet connection!", text_color="red")
        return


# method to start download on click of download button


def download_thread():
    try:
        VIDEO_FOUND.download(SAVE_PATH)

        # Update GUI elements
        showError_Success.configure(text="Download Complete", text_color="green")
    except Exception as e:
        # Update GUI elements
        showError_Success.configure(text="Video is unavailable!", text_color="red")
        print(e)


def startDownload():
    # Create a new thread for the download process
    download_thread_obj = threading.Thread(target=download_thread)
    download_thread_obj.start()

    # Update GUI elements (if needed)
    pPercentage.pack(padx=5, pady=5)
    progressBar.pack(padx=5, pady=5)


def clearEntry():
    url_var.set("")
    showError_Success.configure(text="")

    # Hide the download button and the progress bar
    button_download.pack_forget()
    progressBar.pack_forget()
    pPercentage.pack_forget()
    button_frame.pack_forget()

    # Set the progress bar to zero
    progressBar.set(0)


# initialise elements

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding ui elements
title = customtkinter.CTkLabel(app, text="Enter youtube link")
title.pack(padx=5, pady=5)

# Create a Frame to contain the buttons
textEntry_frame = customtkinter.CTkFrame(app)
textEntry_frame.pack(pady=10)  # Adjust pady as needed

# link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(
    textEntry_frame, width=350, height=40, textvariable=url_var
)

# First Download Button
clearButton = customtkinter.CTkButton(
    textEntry_frame, width=50, height=40, text="clear", command=clearEntry
)

# First Download Button
searchButton = customtkinter.CTkButton(
    textEntry_frame, height=40, text="search", command=searchVideo
)

# Create a Frame to contain the buttons
button_frame = customtkinter.CTkFrame(app)


# Second Download Button
button_download = customtkinter.CTkButton(
    button_frame, text="Download", command=startDownload
)


# Show text output

showError_Success = customtkinter.CTkLabel(app, text="")
showError_Success.pack(padx=5, pady=5)
#
# Progress bar
pPercentage = customtkinter.CTkLabel(app, text="0 %")

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=350)
progressBar.set(0)


# run app
def startMain():
    link.pack(side="left", padx=5)
    clearButton.pack(side="left", padx=5)
    searchButton.pack(side="left", padx=5)

    app.mainloop()


startMain()
