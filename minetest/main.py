""" Main File """

from minetest.minetest_museum import MinetestMuseum
from data_exctration import read_json_file


input_values = read_json_file("datas/input_values.json")
colors = input_values["colors"]
file_name = input_values["file_name"]

minetest = MinetestMuseum()
minetest.config_minetest_objects(file_name, 8, "127.0.0.1", 4711)
# minetest.draw_l_system("A", {"A": "AB", "B": "A"}, 10, 4000, 20, 0, 35, 1)
# minetest.draw_image_l_system("LSA_final.png", 1000, 30, 0)
# minetest.draw_video("datas//Bad Apple.mp4", 100, 30, 0)
minetest.draw_image_l_system("LSA_final.png", -15000, 20, 0)
