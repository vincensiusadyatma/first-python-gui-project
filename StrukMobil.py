from tkinter import *

def btn_clicked():
    print("Button Clicked")
    name = name_entry.get()
    age = age_entry.get()
    duration = duration_entry.get()

    # Membuat jendela baru untuk menampilkan struk
    struk_window = Tk()
    struk_window.geometry("400x300")
    struk_window.configure(bg="#fefbf6")

    # Membuat label-label untuk menampilkan data pada struk
    title_label = Label(struk_window, text="Struk Peminjaman", font=("Arial", 16, "bold"), bg="#fefbf6")
    title_label.pack(pady=10)

    name_label = Label(struk_window, text="Nama: " + name, bg="#fefbf6")
    name_label.pack()

    age_label = Label(struk_window, text="Umur: " + age, bg="#fefbf6")
    age_label.pack()

    duration_label = Label(struk_window, text="Lama Peminjaman: " + duration + " hari", bg="#fefbf6")
    duration_label.pack()

    # Hitung total harga berdasarkan lama peminjaman
    harga_per_hari = 50
    total_harga = int(duration) * harga_per_hari
    harga_label = Label(struk_window, text="Total Harga: Rp" + str(total_harga), bg="#fefbf6")
    harga_label.pack(pady=20)

    struk_window.mainloop()

window = Tk()

window.geometry("1080x720")
window.configure(bg="#fefbf6")
canvas = Canvas(
    window,
    bg="#fefbf6",
    height=720,
    width=1080,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="background.png")
background = canvas.create_image(
    540.0, 360.5,
    image=background_img)

name_entry = Entry(window)
name_entry.place(x=540, y=500)

age_entry = Entry(window)
age_entry.place(x=540, y=530)

duration_entry = Entry(window)
duration_entry.place(x=540, y=560)

submit_button = Button(window, text="Submit", command=btn_clicked)
submit_button.place(x=540, y=590)

window.resizable(False, False)
window.mainloop()
