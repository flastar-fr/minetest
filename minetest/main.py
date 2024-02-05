""" Main File """


from minetest_museum import MinetestMuseum
from data_exctration import read_json_file


input_values = read_json_file("datas/input_values.json")
colors = input_values["colors"]
file_name = input_values["file_name"]

minetest = MinetestMuseum()
minetest.config_minetest_objects(file_name, "127.0.0.1", 4711)
# minetest.draw_l_system("A", {"A": "AB", "B": "A"}, 10, 0, 20, 0, 35, 1)
minetest.draw_image("cercle-de-fleche.png", 100, 20, 0)
