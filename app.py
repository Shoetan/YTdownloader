from tkinter import *

# import the pytube library
from pytube import YouTube

import sys


# create the window
root = Tk()

root.title("YouTube Video Downloader")

root.geometry("500x250")

global v

v = StringVar(root, "1")

SAVE_PATH = "C:/Desktop"

# instructional text
text1 = Label(root, text="Paste link here", padx=20, pady=20)
text1.pack()

# text box to enter the youtube video URL
link_enter = Entry(root, width=50, borderwidth=5)
link_enter.pack()

# Create the download button

btn_download = Button(
    root, text="DOWNLOAD", padx=30, pady=10, command=lambda: download_btn()
)
btn_download.pack()

# create radio buttons

r1 = Radiobutton(
    root, variable=v, text="1080", value=1, padx=10, pady=10, command=lambda: radio1()
).pack()
r2 = Radiobutton(
    root, variable=v, text="720", value=2, padx=10, pady=10, command=lambda: radio2()
).pack()
r1 = Radiobutton(
    root, variable=v, text="360", value=3, padx=10, pady=10, command=lambda: radio3()
).pack()


# create fuctions for the radio buttons and download buttons
def radio1():
    pass


def radio2():
    pass


def radio3():
    pass


def download_btn():
    # get video link from text box
    video_link = link_enter.get()

    video_link = str(video_link)

    # create a object from the youtube class in pytube and pass the video link as a parameter

    url = YouTube(video_link)

    video = url.streams.first()

    video.download(SAVE_PATH)

    Label(root, text="DOWNLOADED", font="arial 15").place(x=180, y=210)


root.mainloop()
