import os
import tkinter as tk
from tkinter.messagebox import showinfo, showerror
from minetest.minetest_museum import MinetestMuseum


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.museum = MinetestMuseum()

        self.geometry('800x600')
        self.title('Minetest Build App')

        self.label = tk.Label(self, text='Minetest Build')
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.generate_image
        self.button.pack()

        self.label = tk.Label(self, text="test")
        self.label.pack()

    def generate_image(self):
        image_file = self.entry.get()

        files = os.listdir(os.getcwd())

        if image_file in files:
            showinfo(title='Information', message=f"{image_file} en cours de construction")
        else:
            showerror(title="Error", message=f"{image_file} n'existe pas dans le dossier de travail")


if __name__ == "__main__":
    app = App()
    app.mainloop()
