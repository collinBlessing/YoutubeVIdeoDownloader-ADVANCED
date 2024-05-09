import tkinter
import customtkinter
import pytube
from pytube import YouTube

SAVE_PATH = '/home/collyne/Downloads'
YT_OBJECT = None
VIDEO_FOUND = None


# noinspection PyUnresolvedReferences

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_downloaded = round(bytes_downloaded / total_size * 100, 2)
    per = str(int(percentage_downloaded))

    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #     update progress bar
    progressBar.set(float(percentage_downloaded / 100))


# noinspection PyUnusedLocal
def searchVideo():
    try:
        showError_Success.configure(text="")
        yt_link = link.get()
        YT_OBJECT = YouTube(yt_link, on_progress_callback=on_progress)
        VIDEO_FOUND = YT_OBJECT.streams.get_highest_resolution()

        # display download button
        button_frame.pack(pady=10) # embedd frame
        button_download.pack(side="left", padx=5)

        # show details here
        print(YT_OBJECT.thumbnail_url)

    except pytube.exceptions.RegexMatchError:
        showError_Success.configure(text="Invalid YouTube link!", text_color="red")

    except pytube.exceptions.VideoUnavailable:
        showError_Success.configure(text="Video is unavailable!", text_color="red")

    except Exception as e:
        showError_Success.configure(text="An error occurred: " + str(e), text_color="red")


def startDownload():
    try:
        VIDEO_FOUND.download(SAVE_PATH)
        pPercentage.pack(padx=5, pady=5)
        progressBar.pack(padx=5, pady=5)

        # Finished downloading label
        showError_Success.configure(text="Download Complete", text_color="green")

    except:
        showError_Success.configure(text="Video is unavailable!", text_color="red")



def clearEntry():
    url_var.set("")
    showError_Success.configure(text="")


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
link = customtkinter.CTkEntry(textEntry_frame, width=350, height=40, textvariable=url_var)

# First Download Button
clearButton = customtkinter.CTkButton(textEntry_frame, width=50, height=40, text="clear", command=clearEntry)

# First Download Button
searchButton = customtkinter.CTkButton(textEntry_frame, height=40, text="search", command=searchVideo)

# Create a Frame to contain the buttons
button_frame = customtkinter.CTkFrame(app)


# Second Download Button
button_download = customtkinter.CTkButton(button_frame, text="Download", command=startDownload)


# Show text output

showError_Success = customtkinter.CTkLabel(app, text="")
showError_Success.pack(padx=5, pady=5)
#
# Progress bar
pPercentage = customtkinter.CTkLabel(app, text="0 %")


progressBar = customtkinter.CTkProgressBar(app, width=350)
progressBar.set(0)



# run app
def startMain():
    link.pack(side="left", padx=5)
    clearButton.pack(side="left", padx=5)
    searchButton.pack(side="left", padx=5)

    app.mainloop()


startMain()
