import os
from os.path import isfile, join
import sys
import tkinter as tk
import glob
from PIL import Image, ImageTk

if (len(sys.argv) <= 1):
    print("No directory provided")
    exit(1)

pathDir = sys.argv[1]

files_list = glob.glob(pathDir + '/**/*', recursive=True)

root = tk.Tk()
root.title("Annotator")

# Opening init image (first opened)
image = Image.open(files_list[0])
image = ImageTk.PhotoImage(image.resize((711, 430)))

image_label = tk.Label(root, image=image, width=711, height=430)
image_label.grid(row=0, columnspan=2)

# Textboxes
font = ("Arial", 20)

textbox_width = 15
textbox_height = 1

firstname = tk.Text(root, height=textbox_height, width=textbox_width, wrap=None, font=font)
firstname_label = tk.Label(text='Имя', font=font)

firstname_label.grid(row=1, column=0)
firstname.grid(row=1, column=1)

secondname = tk.Text(root, height=textbox_height, width=textbox_width, wrap=None, font=font)
secondname_label = tk.Label(text='Фамилия', font=font)

secondname_label.grid(row=2, column=0)
secondname.grid(row=2, column=1)

class_text= tk.Text(root, height=textbox_height, width=textbox_width, wrap=None, font=font)
class_label = tk.Label(text='Класс', font=font)

class_label.grid(row=3, column=0)
class_text.grid(row=3, column=1)

# Button configuration

photo_index = 0

def clear():
    firstname.delete(1.0, tk.END)
    secondname.delete(1.0, tk.END)
    class_text.delete(1.0, tk.END)

def next_photo():
    global photo_index
    global image_label
    photo_index += 1
    print(files_list[photo_index])
    image = ImageTk.PhotoImage(Image.open(files_list[photo_index]).resize((711, 430)))
    image_label.configure(image=image)
    image_label.image = image 
    clear()

def write(*args):
    f = open("data.txt", "a")
    f.write(" ".join(args) + '\n')

def next_photo_and_save():
    write(files_list[photo_index],
          firstname.get(1.0, "end-1c"),
          secondname.get(1.0, "end-1c"),
          class_text.get(1.0, "end-1c"))
    next_photo()

next_photo_button = tk.Button(text="Не сохранять", command=next_photo, font=font)
next_photo_button.grid(row=4, column=0)

save_photo_button = tk.Button(text="Сохранить", command=next_photo_and_save, font=font)
save_photo_button.grid(row=4, column=1)

#---------
root.mainloop()
