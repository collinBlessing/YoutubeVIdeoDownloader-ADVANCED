
from pytube import YouTube


def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        print("Downloading:", yt.title)
        stream.download(output_path)
        print("Download complete!")
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    SAVE_PATH = '/home/collyne/Downloads'

    link = "https://youtu.be/wg2iuU2gazc?si=ZVm70mF9PGwhAO98"

    # video_url = input("Enter the YouTube video URL: ")
    # output_folder = input("Enter the output folder path: ")

    download_video(link, SAVE_PATH)
