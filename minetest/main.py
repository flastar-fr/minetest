""" Main File """
import time

from minetest_museum import MinetestMuseum
from data_exctration import read_json_file
from time import sleep


input_values = read_json_file("datas/input_values.json")
colors = input_values["colors"]
file_name = input_values["file_name"]

minetest = MinetestMuseum()
minetest.config_minetest_objects(file_name, 8, "127.0.0.1", 4711)

minetest.minetest_client.chat_post("Début d'affichage de toutes les créations")

minetest.minetest_client.chat_post("Début construction images")
for _ in range(2):
    minetest.draw_image_2d("LSA_final_V2.png", (0, 150, -20))
    minetest.draw_image_minor_3d("LSA_final_V2.png", (0, 150, 20))
    minetest.draw_image_full_3d("LSA_final_V2.png", (0, 150, 60))
    minetest.draw_image_full_3d("lion.jpg", (0, 150, 100))
minetest.minetest_client.chat_post("Fin construction images")

minetest.draw_image_2d("cercle-de-fleche.png", (250, 250, 140))
minetest.draw_image_2d("cercle-de-fleche.png", (250, 250, -180))

minetest.minetest_client.chat_post("Début construction arbres")
for _ in range(4):
    minetest.draw_l_system_tree((200, 250, -120), 8)
minetest.minetest_client.chat_post("Fin construction arbres")

minetest.minetest_client.chat_post("Début construction suites")
minetest.draw_series((200, 250, -60), lambda n: n**2)
minetest.minetest_client.chat_post("Fin construction suites")

minetest.minetest_client.chat_post("La vidéo commencera dans 10 sec en 200, 250, 160")
sleep(10)
minetest.minetest_client.chat_post("Début vidéo")
minetest.draw_video("Bad Apple.mp4", (200, 250, -160))
minetest.minetest_client.chat_post("Fin vidéo")

minetest.minetest_client.chat_post("Fin d'affichage de toutes les créations")
