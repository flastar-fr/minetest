""" MinetestImage File """
from PIL import Image


class MinetestImage:
    """ Class manager of image
        :attr image: None / Image -> image
    """
    def __init__(self):
        self.image = None

    def open(self, image_name: str):
        """ Method to open and set a datas value
            :param image_name: str -> image file path to input
        """
        image = Image.open(image_name)
        image.load()
        self.image = image.convert("RGB")

    def get_width(self) -> int:
        """ Method to get the image's width
            :return int -> image's width
        """
        assert self.image is not None, "Image is None"
        return self.image.width

    def get_height(self) -> int:
        """ Method to get the image's height
            :return int -> image's height
        """
        assert self.image is not None, "Image is None"
        return self.image.height

    def get_pixel_color(self, x: int, y: int) -> tuple:
        """ Method to get the colors from a pixel
            :param x: int -> x coordinate
            :param y: int -> y coordinate

            :return tuple -> colors in tuple (r, g, b)
        """
        assert self.image is not None, "Image is None"
        return self.image.getpixel((x, y))

    def get_pixel_grayscale(self, x: int, y: int) -> int:
        """ Method to get the grayscale from a pixel
            :param x: int -> x coordinate
            :param y: int -> y coordinate

            :return int -> grayscale value
        """
        pixel_color = self.get_pixel_color(x, y)
        return int(pixel_color[0]*0.3 + pixel_color[1]*0.59 + pixel_color[2]*0.11)
