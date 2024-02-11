""" App File """

import os
import tkinter as tk
import re
import threading
from pathlib import Path
from tkinter.messagebox import showinfo, showerror
from tkinter.simpledialog import askstring
from minetest_museum import MinetestMuseum
from minetest_knn import MinetestKNN
from fileextensionerror import FileExtensionError
from data_exctration import read_json_file


def ask_k_parameter() -> int:
    """ Function to ask the best K parameter for the KNN algorythm
        :return int -> K parameter
    """
    while True:
        result = askstring(title="Paramètre K", prompt='Veuillez renseigner le paramètre K, '
                                                       'veuillez mettre un nombre ou '
                                                       'écrire "k" pour '
                                                       'obtenir le K le plus optimisé (peut prendre du temps)')
        if result == "k":
            input_values = read_json_file("datas/input_values.json")
            file_name = input_values["file_name"]
            minetest_knn = MinetestKNN()
            minetest_knn.open(file_name)

            return minetest_knn.get_best_k()
        try:
            return int(result)
        except ValueError:
            showerror(title="Invalide", message="Paramètre invalide")


def start_thread(to_execute: ..., *args):
    """ Function to execute a thread
        :param to_execute: ... -> object to execute in the new thread
        :param args: Any -> arguments to pass
    """
    threading.Thread(target=to_execute, args=args).start()


class App(tk.Tk):
    def __init__(self, k_parameter: int):
        """ Class app to start an application """
        super().__init__()

        input_values = read_json_file("datas/input_values.json")
        file_name = input_values["file_name"]

        self.museum = MinetestMuseum()
        self.museum.config_minetest_objects(file_name, k_parameter, "127.0.0.1", 4711)

        self.geometry('800x500')
        self.title('Minetest Build App')

        self.image_radiobttn_value = tk.StringVar()
        self.image_radiobttn_value.set("2D")

        game_title_frame = tk.Frame(highlightbackground="black", highlightthickness=1)
        game_title_frame.pack()
        label = tk.Label(game_title_frame, text='Minetest Build')
        label.pack()

        # frames
        image_text_title = tk.Label(text="Générer une image")
        image_text_title.pack(pady=10)
        main_frame_image = tk.Frame(highlightbackground="black", highlightthickness=1)
        main_frame_image.pack()
        frame_generate_image = tk.Frame(main_frame_image)
        frame_generate_image.pack()
        image_button_generate = tk.Button(main_frame_image, text='Générer image')
        image_button_generate['command'] = self.generate_image
        image_button_generate.pack()

        video_text_title = tk.Label(text="Générer une vidéo")
        video_text_title.pack(pady=10)
        main_frame_video = tk.Frame(highlightbackground="black", highlightthickness=1)
        main_frame_video.pack()
        frame_generate_video = tk.Frame(main_frame_video)
        frame_generate_video.pack()
        video_button_generate = tk.Button(main_frame_video, text='Générer vidéo')
        video_button_generate['command'] = self.generate_video
        video_button_generate.pack()

        l_system_text_title = tk.Label(text="Générer un arbre L-System")
        l_system_text_title.pack(pady=10)
        main_frame_l_system = tk.Frame(highlightbackground="black", highlightthickness=1)
        main_frame_l_system.pack()
        frame_generate_l_system = tk.Frame(main_frame_l_system)
        frame_generate_l_system.pack()
        l_system_button_generate = tk.Button(main_frame_l_system, text='Générer arbre')
        l_system_button_generate['command'] = self.generate_l_system_tree
        l_system_button_generate.pack()

        serie_text_title = tk.Label(text="Générer une suite")
        serie_text_title.pack(pady=10)
        main_frame_serie = tk.Frame(highlightbackground="black", highlightthickness=1)
        main_frame_serie.pack()
        frame_generate_serie = tk.Frame(main_frame_serie)
        frame_generate_serie.pack()
        serie_button_generate = tk.Button(main_frame_serie, text='Générer suite')
        serie_button_generate['command'] = self.generate_series
        serie_button_generate.pack()

        # image frame
        image_label_file = tk.Label(frame_generate_image, text="Fichier :")
        image_label_file.grid(row=1, column=0)

        self.image_entry_file = tk.Entry(frame_generate_image)
        self.image_entry_file.grid(row=1, column=1)

        image_radiobtton_lsystem = tk.Radiobutton(frame_generate_image, text="Grayscale",
                                                  variable=self.image_radiobttn_value, value="Grayscale")
        image_radiobtton_lsystem.grid(row=2, column=0)

        image_radiobtton_2d = tk.Radiobutton(frame_generate_image, text="2D",
                                             variable=self.image_radiobttn_value, value="2D")
        image_radiobtton_2d.grid(row=2, column=1)

        image_radiobtton_3d = tk.Radiobutton(frame_generate_image, text="3D L-System et Grayscale",
                                             variable=self.image_radiobttn_value, value="L-System & grayscale")
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

        # frame serie
        serie_label_coords = tk.Label(frame_generate_serie, text="Coordonnées (format : x y z) :")
        serie_label_coords.grid(row=1, column=0)

        self.serie_entry_coords = tk.Entry(frame_generate_serie)
        self.serie_entry_coords.grid(row=1, column=1)

        super().mainloop()

    def generate_image(self):
        """ Method to generate an image following the selected options """
        file = self.image_entry_file.get()
        coords = self.image_entry_coords.get()

        # verification coordinates format
        if re.search(r'^-?\d+ -?\d+ -?\d+$', coords) is None:
            showerror(title="Error", message=f"Le format des coordonnées n'est pas valide")
            return None

        # verification file exists
        files = os.listdir(os.getcwd())
        if file not in files:
            showerror(title='Error', message=f"{file} n'existe pas dans le dossier de travail")
            return None

        path_object = Path(file)
        file_ext = path_object.suffix

        if file_ext not in [".png", ".jpg"]:
            raise FileExtensionError(f"{file_ext} is not supported")

        x, y, z = coords.split(" ")
        x, y, z = int(x), int(y), int(z)

        showinfo(title='Information', message=f"{file} en cours de construction")

        match self.image_radiobttn_value.get():
            case "2D":
                start_thread(self.museum.draw_image_2d, file, (x, y, z))
            case "Grayscale":
                start_thread(self.museum.draw_image_minor_3d, file, (x, y, z))
            case "L-System & grayscale":
                start_thread(self.museum.draw_image_full_3d, file, (x, y, z))

    def generate_video(self):
        """ Method to generate a video following the selected options """
        file = self.video_entry_file.get()
        coords = self.video_entry_coords.get()

        # verification coordinates format
        if re.search(r'^-?\d+ -?\d+ -?\d+$', coords) is None:
            showerror(title="Error", message=f"Le format des coordonnées n'est pas valide")
            return None

        # verification file exists
        files = os.listdir(os.getcwd())
        if file not in files:
            showerror(title='Error', message=f"{file} n'existe pas dans le dossier de travail")
            return None

        path_object = Path(file)
        file_ext = path_object.suffix

        if file_ext not in [".mp4"]:
            raise FileExtensionError(f"{file_ext} is not supported")

        x, y, z = coords.split(" ")
        x, y, z = int(x), int(y), int(z)

        showinfo(title='Information', message=f"{file} en cours de construction")

        start_thread(self.museum.draw_video, file, (x, y, z))

    def generate_l_system_tree(self):
        """ Method to generate a tree using L-System following the selected options """
        iterations = self.l_system_entry_iteration.get()
        coords = self.l_system_entry_coords.get()

        # verification coordinates format
        if re.search(r'^-?\d+ -?\d+ -?\d+$', coords) is None:
            showerror(title="Error", message=f"Le format des coordonnées n'est pas valide")
            return None

        # verification iteration format
        if re.search(r'^\d+$', iterations) is None:
            showerror(title="Error", message=f"Le format de l'itération n'est pas valide")
            return None

        coords = tuple(coords.split(" "))
        iterations = int(iterations)

        if iterations < 5:
            showerror(title="Error", message=f"L'itération doit être supérieur ou égale à 5")
            return None

        showinfo(title='Information', message=f"Arbre en cours de construction")

        start_thread(self.museum.draw_l_system_tree, coords, iterations)

    def generate_series(self):
        """ Method to generate a serie following the selected options """
        coords = self.serie_entry_coords.get()

        # verification coordinates format
        if re.search(r'^-?\d+ -?\d+ -?\d+$', coords) is None:
            showerror(title="Error", message=f"Le format des coordonnées n'est pas valide")
            return None

        x, y, z = coords.split(" ")
        x, y, z = int(x), int(y), int(z)

        start_thread(self.museum.draw_series, (x, y, z), lambda n: n)


if __name__ == "__main__":
    k = ask_k_parameter()
    app = App(k)
