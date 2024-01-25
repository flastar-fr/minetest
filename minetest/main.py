from minetest_knn import MinetestKNN
from minetest_client import MinetestClient
import time


colors = [
    "lightgrey",
    "darkorange",
    "deeppink",
    "lightseagreen",
    "yellow",
    "limegreen",
    "lightcoral",
    "darkgrey",
    "dimgrey",
    "lightseagreen",
    "darkviolet",
    "royalblue",
    "saddlebrown",
    "darkgreen",
    "red",
    "black",
]

minetest_knn = MinetestKNN(colors)
minetest_client = MinetestClient()

# minetest_knn.open("donnees_couleurs.csv")
# best_k = minetest_knn.get_best_k()
# minetest_knn.train_model(best_k)

minetest_client.connect_to("127.0.0.1", 4711)
minetest_client.chat_post("test")

minetest_client.world_destroy_blocks(-200, 10, -200, 200, 40, 200)

minetest_client.disconnect()
