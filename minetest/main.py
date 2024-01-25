""" Main File """

from minetest_knn import MinetestKNN
from minetest_client import MinetestClient
from data_exctration import read_json_file


input_values = read_json_file("input_values.json")
colors = input_values["colors"]
file_name = input_values["file_name"]

minetest_knn = MinetestKNN(colors)
minetest_client = MinetestClient()

minetest_knn.open(file_name)
