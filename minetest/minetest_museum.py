from minetest_knn import MinetestKNN
from minetest_client import MinetestClient
from minetest_image import MinetestImage


class MinetestMuseum:
    def __init__(self):
        self.minetest_knn = MinetestKNN()
        self.minetest_client = MinetestClient()
        self.minetest_image = MinetestImage()

    def config_minetest_objects(self, csv_file: str, ip: str, port: int):
        self.minetest_knn.open(csv_file)
        # self.minetest_knn.train_model(self.minetest_knn.get_best_k())
        self.minetest_knn.train_model(8)
        self.minetest_client.connect_to(ip, port)

    def draw(self, image_file: str, x: int, y: int, z: int):
        self.minetest_image.open(image_file)

        image_width = self.minetest_image.get_width()
        image_height = self.minetest_image.get_height()

        for line in range(image_width):
            for column in range(image_height):
                pixel_colors = self.minetest_image.get_pixel_color(line, column)
                red, green, blue = pixel_colors[0], pixel_colors[1], pixel_colors[2]

                block_data = self.minetest_knn.find_closest_brick_color(red, green, blue)

                z_co = self.minetest_image.get_pixel_grayscale(line, column)
                self.minetest_client.world_set_block(x+line, y+column, z+z_co, 35, block_data[0])
