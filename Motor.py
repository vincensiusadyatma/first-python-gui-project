from tkinter import Tk, Canvas, Button, PhotoImage, Text, StringVar, Entry
from tkinter.messagebox import showinfo
import Data


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Daftar Motor")
        self.geometry("1080x720")
        self.configure(bg="#fefbf6")
        self.canvas = Canvas(self, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.load_images()
        self.create_buttons()
        self.create_entries()

        background = self.canvas.create_image(556.0, 293.5, image=self.background_img)

        self.resizable(False, False)

    def load_images(self):
        self.background_img = PhotoImage(file="background.png", master=self)
        self.img0 = PhotoImage(file="img0.png", master=self)
        self.img1 = PhotoImage(file="img1.png", master=self)
        self.img2 = PhotoImage(file="img2.png", master=self)
        self.img3 = PhotoImage(file="img3.png", master=self)
        self.img4 = PhotoImage(file="img4.png", master=self)
        self.img5 = PhotoImage(file="img5.png", master=self)
        self.img6 = PhotoImage(file="img6.png", master=self)
        self.img7 = PhotoImage(file="img7.png", master=self)
        self.img8 = PhotoImage(file="img8.png", master=self)
        self.img9 = PhotoImage(file="img9.png", master=self)
        self.img10 = PhotoImage(file="img10.png", master=self)
        self.entry0_img = PhotoImage(file="img_textBox0.png", master=self)
        self.entry1_img = PhotoImage(file="img_textBox1.png", master=self)
        self.entry2_img = PhotoImage(file="img_textBox2.png", master=self)
        self.entry3_img = PhotoImage(file="img_textBox3.png", master=self)
        self.entry4_img = PhotoImage(file="img_textBox4.png", master=self)
        self.entry5_img = PhotoImage(file="img_textBox5.png", master=self)

    def create_buttons(self):
        b9 = Button(image=self.img9, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b9.place(x=132, y=249, width=101, height=23)

        b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.btn_clicked2, relief="flat", master=self)
        b0.place(x=139, y=461, width=81, height=23)

        b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.btn_clicked3, relief="flat", master=self)
        b1.place(x=323, y=249, width=92, height=22)

        b4 = Button(image=self.img4, borderwidth=0, highlightthickness=0, command=self.btn_clicked4, relief="flat", master=self)
        b4.place(x=327, y=461, width=81, height=23)

        b2 = Button(image=self.img2, borderwidth=0, highlightthickness=0, command=self.btn_clicked5, relief="flat", master=self)
        b2.place(x=513, y=249, width=97, height=23)

        b5 = Button(image=self.img5, borderwidth=0, highlightthickness=0, command=self.btn_clicked6, relief="flat", master=self)
        b5.place(x=513, y=461, width=81, height=23)

        b3 = Button(image=self.img3, borderwidth=0, highlightthickness=0, command=self.btn_clicked7, relief="flat", master=self)
        b3.place(x=699, y=249, width=90, height=23)

        b7 = Button(image=self.img7, borderwidth=0, highlightthickness=0, command=self.btn_clicked8, relief="flat", master=self)
        b7.place(x=699, y=461, width=81, height=23)

        b6 = Button(image=self.img6, borderwidth=0, highlightthickness=0, command=self.btn_clicked9, relief="flat", master=self)
        b6.place(x=886, y=247, width=81, height=23)

        b8 = Button(image=self.img8, borderwidth=0, highlightthickness=0, command=self.btn_clicked10, relief="flat", master=self)
        b8.place(x=886, y=461, width=81, height=23)





        # b10 = Button(image=self.img10, borderwidth=0, highlightthickness=0, command=self.btn_clicked11, relief="flat", master=self)
        # b10.place(x=841, y=663, width=108, height=23)

    def create_entries(self):
        self.entry0_var = StringVar()
        self.entry0_bg = self.canvas.create_image(893.5, 637.0, image=self.entry0_img)
        entry0 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, master=self, textvariable=self.entry0_var)
        entry0.place(x=761, y=621, width=265, height=30)
        self.canvas.create_text(849.5, 602.5, text="Masukan Lama Peminjaman", fill="#000000", font=("None", int(12.0)))

        self.entry1_var = StringVar()
        self.entry1_bg = self.canvas.create_image(893.5, 560.0, image=self.entry1_img)
        entry1 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, master=self, textvariable=self.entry1_var)
        entry1.place(x=761, y=544, width=265, height=30)
        self.canvas.create_text(850.5, 525.5, text="Masukan Tanggal Peminjaman", fill="#000000", font=("None", int(12.0)))

        self.entry2_var = StringVar()
        self.entry2_bg = self.canvas.create_image(561.5, 637.0, image=self.entry2_img)
        entry2 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, master=self, textvariable=self.entry2_var)
        entry2.place(x=430, y=621, width=263, height=30)
        self.canvas.create_text(520.0, 602.5, text="Masukan Syarat Peminjaman", fill="#000000", font=("None", int(12.0)))

        self.entry3_var = StringVar()
        self.entry3_bg = self.canvas.create_image(560.5, 560.0, image=self.entry3_img)
        entry3 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, master=self, textvariable=self.entry3_var)
        entry3.place(x=428, y=544, width=265, height=30)
        self.canvas.create_text(507.5, 525.5, text="Masukan Alamat", fill="#000000", font=("None", int(12.0)))

        self.entry4_var = StringVar()
        self.entry4_bg = self.canvas.create_image(228.5, 637.0, image=self.entry4_img)
        entry4 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, master=self, textvariable=self.entry4_var)
        entry4.place(x=97, y=621, width=263, height=30)
        self.canvas.create_text(176.5, 602.5, text="Masukan No HP", fill="#000000", font=("None", int(12.0)))

        self.entry5_var = StringVar()
        self.entry5_bg = self.canvas.create_image(227.5, 560.0, image=self.entry5_img)
        entry5 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, master=self, textvariable=self.entry5_var)
        entry5.place(x=95, y=544, width=265, height=30)
        self.canvas.create_text(174.5, 525.5, text="Masukan Nama", fill="#000000", font=("None", int(12.0)))

    def btn_clicked2(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[1] + " " + Data.modelMotor[1]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      1] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[0] + " " + Data.modelMotor[0]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      0] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked3(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[2] + " " + Data.modelMotor[2]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      2] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked4(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[3] + " " + Data.modelMotor[3]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      3] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked5(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[4] + " " + Data.modelMotor[4]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      4] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked6(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[5] + " " + Data.modelMotor[5]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      5] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked7(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[6] + " " + Data.modelMotor[6]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      6] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked8(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[7] + " " + Data.modelMotor[7]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      7] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked9(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[8] + " " + Data.modelMotor[8]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      8] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())

    def btn_clicked10(self):
        showinfo(title="struk persewaan", message="Nama mobil: " + Data.merkMotor[9] + " " + Data.modelMotor[9]
                                                  + "\nNama Peminjam: " + self.entry5_var.get() + "\nNo HP: " + self.entry4_var.get() + "\nAlamat: " + self.entry3_var.get() + "\nSyareat Peminjaman: " + self.entry2_var.get()
                                                  + "\nHarga: " + Data.costMobil[
                                                      9] + "\nLama Peminjaman: " + self.entry0_var.get() + "\n"
                                                  + "Tanggal Peminjaman: " + self.entry1_var.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()