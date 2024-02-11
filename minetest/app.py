import os
import tkinter as tk
from pathlib import Path
from tkinter.messagebox import showinfo, showerror
from minetest.minetest_museum import MinetestMuseum
from fileextensionerror import FileExtensionError


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.museum = MinetestMuseum()

        self.geometry('800x600')
        self.title('Minetest Build App')

        self.label = tk.Label(self, text='Minetest Build')
        self.label.pack()

        # frames
        image_text_title = tk.Label(self, text="Générer une image")
        image_text_title.pack(pady=20)
        frame_generate_image = tk.Frame(borderwidth=3)
        frame_generate_image.pack()
        image_button_generate = tk.Button(text='Générer image')
        image_button_generate['command'] = self.generate_image
        image_button_generate.pack()

        video_text_title = tk.Label(self, text="Générer une vidéo")
        video_text_title.pack(pady=20)
        frame_generate_video = tk.Frame()
        frame_generate_video.pack()
        video_button_generate = tk.Button(text='Générer vidéo')
        video_button_generate['command'] = self.generate_video
        video_button_generate.pack()

        l_system_text_title = tk.Label(self, text="Générer un arbre L-System")
        l_system_text_title.pack(pady=20)
        frame_generate_l_system = tk.Frame()
        frame_generate_l_system.pack()
        l_system_button_generate = tk.Button(text='Générer arbre')
        l_system_button_generate['command'] = self.generate_l_system_tree
        l_system_button_generate.pack()

        function_text_title = tk.Label(self, text="Générer une fonction")
        function_text_title.pack(pady=20)
        frame_generate_function = tk.Frame()
        frame_generate_function.pack()
        function_button_generate = tk.Button(text='Générer fonction')
        function_button_generate['command'] = self.generate_series
        function_button_generate.pack()

        # image frame
        image_label_file = tk.Label(frame_generate_image, text="Fichier :")
        image_label_file.grid(row=1, column=0)

        self.image_entry_file = tk.Entry(frame_generate_image)
        self.image_entry_file.grid(row=1, column=1)

        image_radiobtton_lsystem = tk.Radiobutton(frame_generate_image, text="L-System")
        image_radiobtton_lsystem.grid(row=2, column=0)

        image_radiobtton_2d = tk.Radiobutton(frame_generate_image, text="2D")
        image_radiobtton_2d.grid(row=2, column=1)

        image_radiobtton_3d = tk.Radiobutton(frame_generate_image, text="3D L-System et Grayscale")
        image_radiobtton_3d.grid(row=2, column=2)

        image_label_coords = tk.Label(frame_generate_image, text="Coordonnées (format : x y z) :")
        image_label_coords.grid(row=3, column=0)

        self.image_entry_coords = tk.Entry(frame_generate_image)
        self.image_entry_coords.grid(row=3, column=1)

        # video frame
        video_label_file = tk.Label(frame_generate_video, text="Fichier :")
        video_label_file.grid(row=1, column=0)

        self.video_entry_file = tk.Entry(frame_generate_video)
        self.video_entry_file.grid(row=1, column=1)

        video_label_coords = tk.Label(frame_generate_video, text="Coordonnées (format : x y z) :")
        video_label_coords.grid(row=2, column=0)

        self.video_entry_coords = tk.Entry(frame_generate_video)
        self.video_entry_coords.grid(row=2, column=1)

        # L-System structure
        l_system_label_file = tk.Label(frame_generate_l_system, text="Nombre d'itérations :")
        l_system_label_file.grid(row=1, column=0)

        self.l_system_entry_iteration = tk.Entry(frame_generate_l_system)
        self.l_system_entry_iteration.grid(row=1, column=1)

        l_system_label_coords = tk.Label(frame_generate_l_system, text="Coordonnées (format : x y z) :")
        l_system_label_coords.grid(row=2, column=0)

        self.l_system_entry_coords = tk.Entry(frame_generate_l_system)
        self.l_system_entry_coords.grid(row=2, column=1)

        # frame function
        serie_label_coords = tk.Label(frame_generate_function, text="Coordonnées (format : x y z) :")
        serie_label_coords.grid(row=1, column=0)

        self.serie_entry_coords = tk.Entry(frame_generate_function)
        self.serie_entry_coords.grid(row=1, column=1)

        serie_label_bornes = tk.Label(frame_generate_function,
                                         text="Bornes à afficher (format : x y) :")
        serie_label_bornes.grid(row=2, column=0)

        self.serie_entry_bornes = tk.Entry(frame_generate_function)
        self.serie_entry_bornes.grid(row=2, column=1)

    def generate_image(self):
        file = self.image_entry_file.get()
        coords = self.image_entry_coords.get()

        # faire la vérification regex des coordonnées

        files = os.listdir(os.getcwd())

        if file in files:
            path_object = Path(file)
            file_ext = path_object.suffix

            if file_ext not in [".png", ".jpg"]:
                raise FileExtensionError(f"{file_ext} is not supported")

            x, y, z = coords.split(" ")
            x, y, z = int(x), int(y), int(z)

            showinfo(title='Information', message=f"{file} en cours de construction")

            self.museum.draw_image(file, (x, y, z))
        else:
            showerror(title="Error", message=f"{file} n'existe pas dans le dossier de travail")

    def generate_video(self):
        file = self.video_entry_file.get()
        coords = self.video_entry_coords.get()

        # faire la vérification regex des coordonnées

        files = os.listdir(os.getcwd())

        if file in files:
            path_object = Path(file)
            file_ext = path_object.suffix

            if file_ext not in [".mp4", ".jpg"]:
                raise FileExtensionError(f"{file_ext} is not supported")

            x, y, z = coords.split(" ")
            x, y, z = int(x), int(y), int(z)

            showinfo(title='Information', message=f"{file} en cours de construction")

            self.museum.draw_image(file, (x, y, z))
        else:
            showerror(title='Error', message=f"{file} n'existe pas dans le dossier de travail")

    def generate_l_system_tree(self):
        iterations = self.l_system_entry_iteration.get()
        coords = self.video_entry_coords.get()

        # faire la vérification regex des coordonnées
        # faire la vérification regex de l'iteration

        coords = tuple(coords.split(" "))
        iterations = int(iterations)

        showinfo(title='Information', message=f"arbre en cours de construction")

        self.museum.draw_l_system_tree(coords, "A", iterations)

    def generate_series(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
