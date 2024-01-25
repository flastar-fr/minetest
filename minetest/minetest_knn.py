import pandas as pd
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def distance(x, y):
    """
    renvoie la distance euclidienne entre deux tuples de même taille
    :param x: (tuple)
    :param y: (tuple)
    :return: (float) distance euclidienne
    """
    val = 0
    for i in range(len(x)):
        val += (y[i] - x[i])**2
    return math.sqrt(val)


class MinetestKNN:
    def __init__(self, colors: list):
        self.colors = colors
        self.datas = None
        self.model = None

    def open(self, csv_file: str):
        csv_data = pd.read_csv(f"{csv_file}", delimiter=';')
        self.datas = csv_data

    def find_closest_brick_color(self, red: int, green: int, blue: int, k: int):
        l_choice = self.datas.loc[:, "choice"]

        l_red = self.datas.loc[:, "red"]
        l_green = self.datas.loc[:, "green"]
        l_blue = self.datas.loc[:, "blue"]

        new_datas = (red, green, blue)
        datas = list(zip(l_red, l_green, l_blue))
        l_distances = [distance(new_datas, data) for data in datas]

        l_a_trier = list(zip(l_distances, l_choice))
        l_triee = sorted(l_a_trier, key=lambda data: data[0])

        choices = [data[1] for data in l_triee[:k]]

        colors = {}
        for c in choices:
            colors[c] = colors.get(c, 0) + 1

        prediction = max(colors, key=lambda choice: colors[choice])

        return prediction

    def get_best_k(self):
        l_choice = self.datas.loc[:, "choice"]

        l_red = self.datas.loc[:, "red"]
        l_green = self.datas.loc[:, "green"]
        l_blue = self.datas.loc[:, "blue"]

        # algo knn
        donnees = list(zip(l_red, l_green, l_blue))
        x_train, x_test, y_train, y_test = train_test_split(donnees, l_choice, test_size=0.33, random_state=42)

        result = {}
        for i in range(100):
            k = i + 1

            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(x_train, y_train)
            result[k] = model.score(x_test, y_test)

        # affichage
        maxed = max(result, key=lambda data: result[data])
        return maxed

    def train_model(self, k: int):
        l_choice = self.datas.loc[:, "choice"]

        l_red = self.datas.loc[:, "red"]
        l_green = self.datas.loc[:, "green"]
        l_blue = self.datas.loc[:, "blue"]

        # algo knn
        donnees = list(zip(l_red, l_green, l_blue))
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(donnees, l_choice)

        self.model = model

    def find_closest_brick_color_bis(self, red: int, green: int, blue: int):
        assert self.model is not None, "Model is None"
        prediction = self.model.predict([[red, green, blue]])

        # affichage
        return prediction
