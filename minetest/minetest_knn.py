""" MinetestKNN File """

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


class MinetestKNN:
    """ Class manager of color converter KNN algorithm
        :attr colors: list -> list of all colors
        :attr datas: None / Any -> panda librairies format datas for the KNN algorithm
        :attr model: None / KNeighborsClassifier -> model for the KNN algorithm
    """
    def __init__(self):
        self.datas = None
        self.model = None

    def open(self, csv_file_path: str):
        """ Method to open and set a datas value
            :param csv_file_path: str -> csv file path to input
        """
        csv_data = pd.read_csv(f"{csv_file_path}", delimiter=';')
        self.datas = csv_data

    def get_best_k(self) -> int:
        """ Method to determine the best argument k for the KNN algorithm
            :return int -> the best k result for the KNN algorithm
        """
        # datas extraction
        l_choice = self.datas.loc[:, "choice"]

        l_red = self.datas.loc[:, "red"]
        l_green = self.datas.loc[:, "green"]
        l_blue = self.datas.loc[:, "blue"]

        # knn setup
        donnees = list(zip(l_red, l_green, l_blue))
        x_train, x_test, y_train, y_test = (
            train_test_split(donnees, l_choice, test_size=0.33, random_state=11))

        # tests
        result = {}
        for i in range(len(donnees)//2):
            k = i + 1

            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(x_train, y_train)
            result[k] = model.score(x_test, y_test)

        # get best value
        maxed = max(result, key=lambda data: result[data])
        return maxed

    def train_model(self, k: int):
        """ Method to setup the knn algorithm and training with datas
            :param k: int -> k value to give for KNN algorithm
        """
        # datas extraction
        l_choice = self.datas.loc[:, "choice"]

        l_red = self.datas.loc[:, "red"]
        l_green = self.datas.loc[:, "green"]
        l_blue = self.datas.loc[:, "blue"]

        # knn setup
        donnees = list(zip(l_red, l_green, l_blue))
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(donnees, l_choice)

        self.model = model

    def find_closest_brick_color(self, red: int, green: int, blue: int) -> int:
        """ Method to get the block data based on the color's value input
            :param red: int -> red value (0-255) of the color
            :param green: int -> green value (0-255) of the color
            :param blue: int -> blue value (0-255) of the color

            :return int -> block data
        """
        assert self.model is not None, "Model is None"
        prediction = self.model.predict([[red, green, blue]])

        return prediction
