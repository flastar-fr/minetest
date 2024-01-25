"""
Lycée Saint-André :: TNSI :: Mini-projet KNN/Minecraft
Visualisation des données CSV avec pandas et matplotlib
24/03/2023
"""

# Libraries
import pandas as pd
import matplotlib.pyplot as plt


# Ouverture et lecture des données CSV depuis un fichier
csv_data = pd.read_csv("test//donnees_couleurs.csv", delimiter=';')

# Préparation du graphique 3D
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
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

# Ajout des points
for index, ligne in csv_data.iterrows():
    xr = ligne["red"]
    yg = ligne["green"]
    zb = ligne["blue"]
    m = 'o'
    ax.scatter(xr, yg, zb, marker=m, c=colors[ligne["choice"]])

# Configuration des axes
ax.set_xlabel("Red")
ax.set_ylabel("Green")
ax.set_zlabel("Blue")

# Affichage du graphique 3D
plt.show()
