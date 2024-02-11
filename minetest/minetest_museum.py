""" MinetestMuseum File """

from minetest_knn import MinetestKNN
from minetest_client import MinetestClient
from minetest_image import MinetestImage
from data_exctration import reduce_frame_rate
from math import dist


def l_system(axiom: str, rules: dict, iterations: int) -> str:
    """ Function to apply rules from a L-System on an axiom a certain amount of time
        :param axiom: str -> first input to change
        :param rules: dict -> rules followed by the axiom
        :param iterations: int -> the amount of time the program runs

        :return L-System output
    """
    to_return = ""
    for i in range(iterations):
        to_return = ""
        for c in axiom:
            if c in rules.keys():
                replace = rules[c]
                to_return += replace
            else:
                to_return += c
        axiom = to_return
    return to_return


class MinetestMuseum:
    """ Class manager of the museum
        :attr colors: list -> list of all colors
        :attr datas: None / Any -> panda librairies format datas for the KNN algorithm
        :attr model: None / KNeighborsClassifier -> model for the KNN algorithm

        :method config_minetest_objects -> initialize all the main objects
        :method draw_image -> draw an image file at the given coordinates
        :method draw_image_l_system -> draw an image file using L-System at the given coordinates
        :method draw_l_system -> draw a simple structure using L-System
    """

    def __init__(self):
        self.minetest_knn = MinetestKNN()
        self.minetest_client = MinetestClient()
        self.minetest_image = MinetestImage()

    def config_minetest_objects(self, csv_file: str, k: int, ip: str, port: int):
        """ Method to configure the objects
            :param csv_file: str -> csv file path of the training KNN algorithm datas
            :param k: int -> k paramater for the KNN algorithm
            :param ip: str -> ip to connect
            :param port: int -> port to enter
        """
        self.minetest_client.connect_to(ip, port)
        self.minetest_client.chat_post("Connexion réussi")
        self.minetest_client.chat_post("Initialisation du KNN (peut prendre du temps)")
        self.minetest_knn.open(csv_file)
        self.minetest_knn.train_model(k)
        self.minetest_client.chat_post("Initialisation du KNN réussi")
        self.minetest_client.chat_post("Musée opérationnel")

    def draw_image_2d(self, image_file: str, coords: tuple):
        """ Method to draw a 2d image in Minetest at the given coordinates
            :param image_file: str -> image path to draw in Minetest
            :param coords: tuple -> x, y, z coordinates
        """
        self.minetest_image.open(image_file)

        image_width = self.minetest_image.get_width()
        image_height = self.minetest_image.get_height()

        x, y, z = coords

        y += image_height  # reverse image
        # draw
        self.minetest_client.chat_post(f"{image_file} en cours de construction")
        for line in range(image_width):
            for column in range(image_height):
                pixel_colors = self.minetest_image.get_pixel_color(line, column)
                if pixel_colors[-1] > 0:  # don't show if the pixel is transparente (remove background)
                    red, green, blue = pixel_colors[0], pixel_colors[1], pixel_colors[2]

                    block_data = self.minetest_knn.find_closest_brick_color(red, green, blue)

                    self.minetest_client.world_set_block(x + line, y - column, z, 35, block_data)

        self.minetest_client.chat_post(f"{image_file} est terminé")

    def draw_image_minor_3d(self, image_file: str, coords: tuple):
        """ Method to draw an image in Minetest in 3d using grayscale and columns at the given coordinates
            :param image_file: str -> image path to draw in Minetest
            :param coords: tuple -> x, y, z coordinates
        """
        self.minetest_image.open(image_file)

        image_width = self.minetest_image.get_width()
        image_height = self.minetest_image.get_height()

        x, y, z = coords

        y += image_height  # reverse image
        # draw
        self.minetest_client.chat_post(f"{image_file} en cours de construction")
        for line in range(image_width):
            for column in range(image_height):
                pixel_colors = self.minetest_image.get_pixel_color(line, column)
                if pixel_colors[-1] > 0:  # don't show if the pixel is transparente (remove background)
                    red, green, blue = pixel_colors[0], pixel_colors[1], pixel_colors[2]

                    block_data = self.minetest_knn.find_closest_brick_color(red, green, blue)

                    grsc_val = self.minetest_image.get_pixel_grayscale(line, column) // 100  # grayscale

                    self.minetest_client.world_set_blocks(x + line, y - column, z + grsc_val, x + line,
                                                          y - column, z, 35, block_data)

        self.minetest_client.chat_post(f"{image_file} est terminé")

    def draw_image_full_3d(self, image_file: str, coords: tuple):
        """ Method to draw a 3d image in Minetest using l-system, grayscale and columns at the given coordinates
            :param image_file: str -> image path to draw in Minetest
            :param coords: tuple -> x, y, z coordinates
        """
        self.minetest_image.open(image_file)

        image_width = self.minetest_image.get_width()
        image_height = self.minetest_image.get_height()

        x, y, z = coords

        y += image_height  # reverse image
        # draw
        self.minetest_client.chat_post(f"{image_file} en cours de construction")
        for line in range(image_width):
            for column in range(image_height):
                pixel_colors = self.minetest_image.get_pixel_color(line, column)
                if pixel_colors[-1] > 0:  # don't show if the pixel is transparente (remove background)
                    red, green, blue = pixel_colors[0], pixel_colors[1], pixel_colors[2]

                    block_data = self.minetest_knn.find_closest_brick_color(red, green, blue)

                    grsc_val = self.minetest_image.get_pixel_grayscale(line, column) // 100  # grayscale

                    self.draw_basic_l_system("A", {"A": "AB", "B": "A"}, grsc_val,
                                             (x+line, y-column, z+grsc_val),
                                             35, block_data)

                    self.minetest_client.world_set_blocks(x+line, y-column, z+grsc_val+1, x+line,
                                                          y-column, z, 35, block_data)

        self.minetest_client.chat_post(f"{image_file} est terminé")

    def draw_basic_l_system(self, axiom: str, rules: dict, iterations: int,
                            coords: tuple, block_id: int, block_data: int = 1):
        """ Method to draw a basic L-System structure
            :param axiom: str -> default value to use in the L-System
            :param rules: dict -> rules to follow in the L-System
            :param iterations: int -> amount of rules executions
            :param coords: tuple -> x, y, z coordinates
            :param block_id: int -> decide which block to use
            :param block_data: int -> decide which varient (if it has) to use
        """
        characters = l_system(axiom, rules, iterations)
        x, y, z = coords

        for c in characters:
            match c:
                case "A":
                    x += 1
                    y += 1
                case "B":
                    y -= 1
                    z += 1
            self.minetest_client.world_set_block(x, y, z, block_id, block_data)

    def draw_video(self, video_file: str, coords: tuple):
        """ Method to draw a video in Minetest (preferably, black and white)
            :param video_file: str -> video file path
            :param coords: tuple -> x, y, z coordinates
        """
        # turn current video into 3 FPS video
        self.minetest_client.chat_post("Début de la conversion")
        video = reduce_frame_rate(video_file, 3)
        self.minetest_client.chat_post("Fin de la conversion")

        # initialize variables
        size = video.size
        x_values = [x for x in range(0, size[0], size[0] // 40)]
        y_values = [y for y in reversed(range(0, size[1], size[1] // 32))]

        previous_frame = [[15 for _ in y_values] for _ in x_values]
        x, y, z = coords

        # draw
        self.minetest_client.chat_post("Début de l'affichage")
        for line in range(len(previous_frame)):
            for column in range(len(previous_frame[0])):
                self.minetest_client.world_set_block(line+x, column+y, z, 35, 15)

        for frame in video.iter_frames(fps=3):
            self.minetest_image.open_image_from_array(frame)

            # get current frame
            current_frame = []
            for i, x_image in enumerate(x_values):
                current_frame.append([])
                for j, y_image in enumerate(y_values):
                    pixel_color = self.minetest_image.get_pixel_color(x_image, y_image)
                    red, green, blue = pixel_color

                    block_data = self.minetest_knn.find_closest_brick_color(red, green, blue)

                    match block_data:
                        case 6:
                            block_data = 0
                        case 13:
                            block_data = 15
                        case 5:
                            block_data = 0

                    current_frame[i].append(block_data)

                    if previous_frame[i][j] != block_data:
                        self.minetest_client.world_set_block(x+i, y+j, z, 35, block_data)

            previous_frame = current_frame

        video.close()
        self.minetest_client.chat_post("Fin de l'affichage")

    def draw_l_system_tree(self, coords: tuple, iterations: int):
        """ Method to draw a tree using L-System at the given coordinates
            :param coords: tuple -> x, y, z coordinates
            :param iterations: int -> amount of iterations for L-System (tree size)
        """
        assert iterations > 5, "Iterations must be higher than 5"
        characters = l_system("A", {"A": "AB", "B": "AC"}, iterations)
        characters = "A" * int(iterations*1.5) + characters   # add a higher trunk

        x, y, z = coords
        x, y, z = int(x), int(y), int(z)

        nb_c_char = characters.count("C")

        # draw tree
        for char in characters:
            branch_lenght = "F" * int(nb_c_char // 2)

            match char:
                case "A":
                    if branch_lenght not in ["F", ""]:
                        self.minetest_client.world_set_blocks(x - 1, y, z - 1, x + 1, y, z + 1, 17, 2)
                    else:
                        self.minetest_client.world_set_block(x, y, z, 17, 2)
                case "B":
                    if branch_lenght not in ["F", ""]:
                        self.minetest_client.world_set_blocks(x - 1, y, z - 1, x + 1, y, z + 1, 17, 2)
                    else:
                        self.minetest_client.world_set_block(x, y, z, 17, 2)
                case "C":
                    if branch_lenght not in ["F", ""]:
                        self.minetest_client.world_set_blocks(x - 1, y, z - 1, x + 1, y, z + 1, 17, 2)
                        self._draw_l_system_branch((x, y, z), "A/A/A/A/A/A/A/A/A",
                                                   {"A": "[BBBB]", "B": f"[{branch_lenght}]"})
                    else:
                        self.minetest_client.world_set_block(x, y, z, 17, 2)

                    nb_c_char -= 1

            y += 1

    def _draw_l_system_branch(self, coords: tuple, axiom: str, rules: dict):
        """ Private method to draw the branches of the tree following the axiom, rules and coordinates
            :param coords: tuple -> x, y, z coordinates
            :param axiom: str -> first input to change
            :param rules: dict -> rules followed by the axiom
        """
        x_trunk, y_trunk, z_trunk = coords

        characters = l_system(axiom, rules, 2)

        stack = []

        # facing initialize
        facings = {"N": (0, 0, 1), "S": (0, 0, -1), "E": (1, 0, 0), "W": (-1, 0, 0),
                   "NE": (1, 0, 1), "NW": (-1, 0, 1), "SE": (1, 0, -1), "SW": (-1, 0, -1)}
        facings_list = ["W", "NW", "N", "NE", "E", "SE", "S", "SW"]
        index = 2
        facing = facings_list[index]

        # draw
        for char in characters:
            match char:
                case "[":
                    stack.append((x_trunk, y_trunk, z_trunk, facing))
                case "]":
                    x_trunk, y_trunk, z_trunk, facing = stack.pop()
                case "/":
                    index += 1
                    if index >= len(facings_list):
                        index = 0
                    facing = facings_list[index]
                case "F":
                    facing_coordinates = facings[facing]
                    x_trunk += facing_coordinates[0]
                    y_trunk += -1
                    z_trunk += facing_coordinates[2]
                    self.minetest_client.world_set_block(x_trunk, y_trunk, z_trunk,
                                                         17, 2)

    def draw_series(self, coords: tuple, expression: ...):
        """ Method to draw a serie at the given coordinates between 2 points in 100 blocs
            :param coords: tuple -> x, y, z coordinates
            :param expression: Any -> serie to draw
        """
        left_int = -50
        right_int = 50
        step = int(dist([left_int], [right_int])//100)
        step = 1 if step == 0 else step

        x, y, z = coords

        # draw axis
        self.minetest_client.world_set_blocks(x-50, y, z+1, x+50, y,
                                              z+1, 35, 15)
        self.minetest_client.world_set_blocks(x, y-50, z+1, x, y+50,
                                              z+1, 35, 15)

        # draw arrows
        self.minetest_client.world_set_block(x+right_int-1, y+1, z+1, 35, 15)
        self.minetest_client.world_set_block(x+right_int-1, y-1, z+1, 35, 15)
        self.minetest_client.world_set_block(x+right_int-2, y+2, z+1, 35, 15)
        self.minetest_client.world_set_block(x+right_int-2, y-2, z+1, 35, 15)

        self.minetest_client.world_set_block(x-1, y-1+max(left_int, right_int), z+1,
                                             35, 15)
        self.minetest_client.world_set_block(x+1, y-1+max(left_int, right_int), z+1,
                                             35, 15)
        self.minetest_client.world_set_block(x-2, y-2+max(left_int, right_int), z+1,
                                             35, 15)
        self.minetest_client.world_set_block(x+2, y-2+max(left_int, right_int), z+1,
                                             35, 15)

        # draw serie
        x += left_int
        for value in range(left_int, right_int, step):
            try:
                val = expression(value)
                if val < y+50:
                    self.minetest_client.world_set_block(x, int(y+val), z, 35, 9)
            except ZeroDivisionError:
                continue
            x += 1
