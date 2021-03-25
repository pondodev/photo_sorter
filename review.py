#!/usr/bin/python

import tkinter
from PIL import ImageTk, Image
import os

# globals
image_index = 0
image_files = []
image_directory = "./images/"
max_image_size = 1024, 1024

# button functions
def approve():
    # do approval stuff here
    print("approving " + image_files[image_index])
    os.rename(image_directory + image_files[image_index], "./approved/" + image_files[image_index])
    next_image()

def deny():
    # do denial stuff here
    print("denying " + image_files[image_index])
    os.rename(image_directory + image_files[image_index], "./denied/" + image_files[image_index])
    next_image()

def next_image():
    global image_index
    # increment index
    image_index += 1

    # change image around
    to_resize = Image.open(image_directory + image_files[image_index])
    to_resize.thumbnail(max_image_size, Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(to_resize)
    picture_display.configure(image=new_img)
    picture_display.image = new_img
    picture_display.photo_ref = new_img

    # display new title
    title["text"] = "current image: " + image_files[image_index]

# program logic init
print("loading image data...")
image_files = os.listdir(image_directory)
print("creating directories...")
try:
    os.mkdir("./approved")
    print("made approved directory")
except:
    print("approved directory probably already exists")

try:
    os.mkdir("./denied")
    print("made denied directory")
except:
    print("denied directory probably already exists")

# window init
print("starting window...")
window = tkinter.Tk()

title = tkinter.Label(text="current image: " + image_files[image_index])
title.pack()

btn_yeah = tkinter.Button(text="yeah", command=approve)
btn_yeah.pack()

btn_nah = tkinter.Button(text="nah", command=deny)
btn_nah.pack()

btn_skip = tkinter.Button(text="skip", command=next_image)
btn_skip.pack()

to_resize = Image.open(image_directory + image_files[image_index])
to_resize.thumbnail(max_image_size, Image.ANTIALIAS)
img = ImageTk.PhotoImage(to_resize)
picture_display = tkinter.Label(window, image=img, pady=10)
picture_display.pack(side=tkinter.TOP);

# event loop
window.mainloop()
