import os
import tkinter as tk
from pathlib import Path
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

        # frame

        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.generate
        self.button.pack()

        self.label = tk.Label(self, text="test")
        self.label.pack()

    def generate(self):
        file = self.entry.get()

        files = os.listdir(os.getcwd())

        if file in files:
            showinfo(title='Information', message=f"{file} en cours de construction")
        else:
            showerror(title="Error", message=f"{file} n'existe pas dans le dossier de travail")

        path_object = Path(file)
        file_ext = path_object.suffix


if __name__ == "__main__":
    app = App()
    app.mainloop()
