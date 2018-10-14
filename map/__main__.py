from tkinter import *
from PIL import Image, ImageTk
from config import Config


def create_path(x, y, z):
    return Config.MAP_PATH.value + str(z) + "/" + str(x) + "/" + str(y) + ".png"


def draw(x, y, z):
    photo1 = ImageTk.PhotoImage(Image.open(create_path(x, y + 1, z)))
    label_image.config(image=photo1)
    label_image.photo = photo1

    photo2 = ImageTk.PhotoImage(Image.open(create_path(x, y, z)))
    label_second.config(image=photo2)
    label_second.photo = photo2

    photo3 = ImageTk.PhotoImage(Image.open(create_path(x + 1, y + 1, z)))
    label_third.config(image=photo3)
    label_third.photo = photo3

    photo4 = ImageTk.PhotoImage(Image.open(create_path(x + 1, y, z)))
    label_fourth.config(image=photo4)
    label_fourth.photo = photo4


def command_increase(event):
    global x, y, z

    if z < Config.NUMBER_OF_LAYERS.value:
        z += 1
        x = x * 2 + 1
        y = y * 2 + 1
    draw(x, y, z)


def command_decrease(event):
    global x, y, z
    xc = x
    yc = y
    x = int(x / 2)
    y = int(y / 2)
    if z > 1:
        z -= 1
        if yc > 2 ** z - 3:
            y = y - 1 if y > 0 else 0
        if xc > 2 ** z - 3:
            x = x - 1 if x > 0 else 0

    draw(x, y, z)


def command_up(event):
    global x
    global y
    global z

    if y < 2 ** z - 2:
        y += 1
    draw(x, y, z)


def command_right(event):
    global x
    global y
    global z

    if x < 2 ** z - 2:
        x += 1
    draw(x, y, z)


def command_down(event):
    global x
    global y
    global z

    if y > 0:
        y -= 1
    draw(x, y, z)


def command_left(event):
    global x
    global y
    global z

    if x > 0:
        x -= 1
    draw(x, y, z)


root = Tk()

global x, y, z

if __name__ == "__main__":
    x = 0
    y = 0
    z = 1
    image1 = Image.open(create_path(x, y + 1, z))
    root.geometry('%dx%d' % (image1.size[0] + image1.size[0] + 500, image1.size[1] + image1.size[1] + 600))
    tkpi = ImageTk.PhotoImage(image1)
    label_image = Label(root, image=tkpi)
    label_image.place(x=250, y=70, width=image1.size[0], height=image1.size[1])

    image2 = Image.open(create_path(x, y, z))
    second_photo = ImageTk.PhotoImage(image2)
    label_second = Label(root, image=second_photo)
    label_second.place(x=250, y=70 + image1.size[1], width=image2.size[0], height=image2.size[1])

    image3 = Image.open(create_path(x + 1, y + 1, z))
    third_photo = ImageTk.PhotoImage(image3)
    label_third = Label(root, image=third_photo)
    label_third.place(x=250 + image1.size[0], y=70, width=image3.size[0], height=image3.size[1])

    image4 = Image.open(create_path(x + 1, y, z))
    fourth_photo = ImageTk.PhotoImage(image4)
    label_fourth = Label(root, image=fourth_photo)
    label_fourth.place(x=250 + image1.size[0], y=70 + image1.size[1], width=image4.size[0], height=image4.size[1])

    Button_Up = Button(root, text="UP", width=7)
    Button_Up.grid(row=0, column=1)
    Button_Up.bind("<Button-1>", command_up)

    Button_Down = Button(root, text="DOWN", width=7)
    Button_Down.grid(row=2, column=1)
    Button_Down.bind("<Button-1>", command_down)

    Button_Left = Button(root, text="LEFT", width=7)
    Button_Left.grid(row=1, column=0)
    Button_Left.bind("<Button-1>", command_left)

    Button_Right = Button(root, text="RIGHT", width=7)
    Button_Right.grid(row=1, column=3)
    Button_Right.bind("<Button-1>", command_right)

    Button_increase = Button(root, text="+", width=7)
    Button_increase.grid(row=6, column=1)
    Button_increase.bind("<Button-1>", command_increase)

    Button_decrease = Button(root, text="-", width=7)
    Button_decrease.grid(row=7, column=1)
    Button_decrease.bind("<Button-1>", command_decrease)

    root.mainloop()
