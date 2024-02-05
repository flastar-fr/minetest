""" Museum Main File """
from minetest_knn import MinetestKNN
from minetest_client import MinetestClient
from minetest_image import MinetestImage


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
            replace = rules[c]
            to_return += replace
            axiom = to_return

    return to_return


class MinetestMuseum:
    """ Class manager of the museum
        :attr colors: list -> list of all colors
        :attr datas: None / Any -> panda librairies format datas for the KNN algorithm
        :attr model: None / KNeighborsClassifier -> model for the KNN algorithm

        :method config_minetest_objects -> initialize all the main objects
        :method draw_image -> draw an image file at the given coordinates
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
        self.minetest_knn.open(csv_file)
        self.minetest_knn.train_model(k)
        self.minetest_client.connect_to(ip, port)

    def draw_image(self, image_file: str, x: int, y: int, z: int):
        """ Method to draw an image in Minetest at the given coordinates
            :param image_file: str -> image path to draw in Minetest
            :param x: int -> x coordinate
            :param y: int -> y coordinate
            :param z: int -> z coordinate
        """
        self.minetest_image.open(image_file)

        image_width = self.minetest_image.get_width()
        image_height = self.minetest_image.get_height()

        # image process
        for line in range(image_width):
            for column in reversed(range(image_height)):
                pixel_colors = self.minetest_image.get_pixel_color(line, column)
                if pixel_colors[-1] == 255:     # don't show if the pixel is transparente
                    red, green, blue = pixel_colors[0], pixel_colors[1], pixel_colors[2]

                    block_data = self.minetest_knn.find_closest_brick_color(red, green, blue)

                    grsc_val = self.minetest_image.get_pixel_grayscale(line, column)//100    # grayscale

                    self.minetest_client.world_set_block(x+line, y+column, z+grsc_val, 35, block_data)

    def draw_l_system(self, axiom: str, rules: dict, iterations: int,
                      x: int, y: int, z: int, block_id: int, block_data: int = 1):
        """ Method to draw a basic L-System structure
        :param axiom: str -> default value to use in the L-System
        :param rules: dict -> rules to follow in the L-System
        :param iterations: int -> amount of rules executions
        :param x: int -> x coordinate
        :param y: int -> y coordinate
        :param z: int -> z coordinate
        :param block_id: int -> decide which block to use
        :param block_data: int -> decide which varient (if it has) to use
        """

        characters = l_system(axiom, rules, iterations)

        for c in characters:
            match c:
                case "A":
                    x += 1
                    y += 1
                case "B":
                    y -= 1
                    z += 1
            self.minetest_client.world_set_block(x, y, z, block_id, block_data)
