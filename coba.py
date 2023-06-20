# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:39:45 2023

@author: adyat
"""

from tkinter import *


def btn_clicked():
    print("1")

def btn_clicked2():
    print("2")

def btn_clicked3():
    print("3")

def btn_clicked4():
    print("4")

def btn_clicked5():
    print("5")

def btn_clicked6():
    print("6")

def btn_clicked7():
    print("7")

def btn_clicked8():
    print("8")

def btn_clicked9():
    print("9")

def btn_clicked10():
    print("10")

def btn_clicked11():
    print("11")


window = Tk()

window.geometry("1080x720")
window.configure(bg="#fefbf6")
canvas = Canvas(window, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(541.5, 270.5, image=background_img)

img0 = PhotoImage(file=f"img0.png")
b0 = Button( image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b0.place(x=118, y=226, width=101, height=23)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=btn_clicked2, relief="flat")
b1.place(x=309, y=226, width=92, height=22)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=btn_clicked3, relief="flat")
b2.place(x=872, y=438, width=81, height=23)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=btn_clicked4, relief="flat")
b3.place(x=685, y=438, width=81, height=23)

img4 = PhotoImage(file=f"img4.png")
b4 = Button(image=img4, borderwidth=0, highlightthickness=0, command=btn_clicked5, relief="flat")
b4.place(x=872, y=224, width=81, height=23)

img5 = PhotoImage(file=f"img5.png")
b5 = Button(image=img5, borderwidth=0, highlightthickness=0, command=btn_clicked6, relief="flat")
b5.place(x=499, y=438, width=81, height=23)

img6 = PhotoImage(file=f"img6.png")
b6 = Button(image=img6, borderwidth=0, highlightthickness=0, command=btn_clicked7, relief="flat")
b6.place(x=313, y=438, width=81, height=23)

img7 = PhotoImage(file=f"img7.png")
b7 = Button(image=img7, borderwidth=0, highlightthickness=0, command=btn_clicked8, relief="flat")
b7.place(x=125, y=438, width=81, height=23)

img8 = PhotoImage(file=f"img8.png")
b8 = Button(image=img8, borderwidth=0, highlightthickness=0, command=btn_clicked9, relief="flat")
b8.place(x=685, y=226, width=90, height=23)

img9 = PhotoImage(file=f"img9.png")
b9 = Button(image=img9, borderwidth=0, highlightthickness=0, command=btn_clicked10, relief="flat")
b9.place(x=499, y=226, width=97, height=23)

img10 = PhotoImage(file=f"img10.png")
b10 = Button(image=img10, borderwidth=0, highlightthickness=0, command=btn_clicked11, relief="flat")
b10.place(x=893, y=668, width=108, height=23)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(870.5, 605.0, image=entry0_img)
entry0 = Text(bd=0, bg="#d9d9d9", highlightthickness=0)
entry0.place(x=738, y=589, width=265, height=30)

canvas.create_text(826.5, 575.5, text="Masukan Lama Peminjaman", fill="#000000", font=("None", int(12.0)))

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(870.5, 535.5, image=entry1_img)
entry1 = Text(bd=0, bg="#d9d9d9", highlightthickness=0)
entry1.place(x=739, y=521, width=263, height=27)

canvas.create_text(826.0, 504.5, text="Masukan Tanggal Peminjaman", fill="#000000", font=("None", int(12.0)))

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(538.5, 606.5, image=entry2_img)
entry2 = Text(bd=0, bg="#d9d9d9", highlightthickness=0)
entry2.place(x=407, y=592, width=263, height=27)

canvas.create_text(510.0, 575.5, text="Apakah Anda ingin Menambah Supir", fill="#000000", font=("None", int(12.0)))

entry3_img = PhotoImage(file=f"img_textBox3.png")
entry3_bg = canvas.create_image(537.5, 535.5, image=entry3_img)
entry3 = Text(bd=0, bg="#d9d9d9", highlightthickness=0)
entry3.place(x=407, y=521, width=261, height=27)

canvas.create_text(494.5, 504.5, text="Masukan Syarat Peminjaman", fill="#000000", font=("None", int(12.0)))

entry4_img = PhotoImage(file=f"img_textBox4.png")
entry4_bg = canvas.create_image(213.5, 668.5, image=entry4_img)
entry4 = Text(bd=0, bg="#d9d9d9", highlightthickness=0)
entry4.place(x=82, y=654, width=263, height=27)

canvas.create_text(161.0, 637.5, text="Masukan Alamat", fill="#000000", font=("None", int(12.0)))

entry5_img = PhotoImage(file=f"img_textBox5.png")
entry5_bg = canvas.create_image(212.5, 606.5, image=entry5_img)
entry5 = Text(bd=0, bg="#d9d9d9", highlightthickness=0)
entry5.place(x=82, y=592, width=261, height=27)

canvas.create_text(160.0, 574.5, text="Masukan No HP", fill="#000000", font=("None", int(12.0)))

entry6_img = PhotoImage(file=f"img_textBox6.png")
entry6_bg = canvas.create_image(213.5, 535.5, image=entry6_img)
entry6 = Text(bd=0, bg="#d9d9d9", highlightthickness=0)
entry6.place(x=82, y=521, width=263, height=27)

canvas.create_text(161.0, 504.5, text="Masukan Nama", fill="#000000", font=("None", int(12.0)))

window.resizable(False, False)
window.mainloop()