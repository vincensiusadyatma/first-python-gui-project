from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1080x720")
window.configure(bg = "#fefbf6")
canvas = Canvas(
    window,
    bg = "#fefbf6",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    540.0, 360.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()

