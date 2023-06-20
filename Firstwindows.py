from tkinter import Tk, Canvas, Button, PhotoImage


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.configure(bg="#fefbf6")

        self.canvas = Canvas(self, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)

        self.load_images()
        self.create_buttons()
        

        self.resizable(False, False)
        self.mainloop()

    def load_images(self):
        self.img0 = PhotoImage(file="motorButton.png", master=self)
        self.img1 = PhotoImage(file="MobilButton.png", master=self)
        self.background_img = PhotoImage(file="backgroundMenu.png", master=self)

    def create_buttons(self):
        b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.btn_Motor, relief="flat", master=self)
        b0.place(x=80, y=552, width=398, height=102)

        b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.btn_Mobil, relief="flat", master=self)
        b1.place(x=600, y=552, width=398, height=102)

        background = self.canvas.create_image(546, 320, image=self.background_img)

    def btn_Motor(self):
        from Motor import App
        App().mainloop()

    def btn_Mobil(self):
        from Mobil import App
        App().mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()