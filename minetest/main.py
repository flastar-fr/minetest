""" Main File """

from minetest_knn import MinetestKNN
from minetest_client import MinetestClient
from minetest_museum import MinetestMuseum
from data_exctration import read_json_file


input_values = read_json_file("datas/input_values.json")
colors = input_values["colors"]
file_name = input_values["file_name"]

minetest = MinetestMuseum()
minetest.config_minetest_objects(file_name, "127.0.0.1", 4711)
minetest.draw("cercle-de-fleche.png", 30, 100, 50)
