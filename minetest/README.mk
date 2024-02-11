# Minetest Builder
## Lancer le projet
Le projet utilise la librairie [```moviepy```](https://pypi.org/project/moviepy/) pour lire une vidéo et la manipuler. Il est alors nécessaire de l'installer pour pouvoir exécuter le programme.
Pour cela il faut exécuter la commande :
```pip install moviepy```
Ou alors l'installer à l'aide du fichier requirement.txt présent dans le projet avec la commande en se plaçant dans le même dossier que le fichier :
```pip install requirement.txt```
Il est également possible d'installer cette librairie directement via l'IDE PyCharm depuis le menu ```Python Packages```.

## Type de constructions
Le projet comporte 5 types de constructions différents, l'image, le L-System, la vidéo, l'arbre et la suite.
### Construction d'une image
La construction d'une image comporte 3 variantes différentes symbolisés par 3 méthodes de la classe ```MinetestMuseum``` différentes qui sont :
- ```draw_image_2d``` permettant la construction d'une image en 2 dimensions
- ```draw_image_minor_3d``` permettant la construction d'une image en 3 dimensions utilisant le principe de grayscale et de colonnes
- ```draw_image_full_3d``` permettant la construction d'une image en 3 dimensions utilisant à la fois le grayscale et les colonnes mais aussi les L-System
L'image aura pour coordonnées le point le plus en bas à gauche spécifié au moment de l'appelle de la méthode.

### Construction d'une structure simple de L-System
Cette structure bien que pouvant être construit indépendamment est principalement faite pour être utilisé leur de la création d'images 3d cependant il est possible d'y gérer les règles élémentaires d'un L-System c'est à dire l'axiom, les règles et l'itérations.
Les structures choisies lors de la génération d'image ont ces paramètres :
> axiom = "A"
> règles = {"A": "AB", "B": "A"}
> itérations = grayscale // 100

### Construction d'une vidéo
Les vidéos choisies doivent de préférence être en noir et blanc puisqu'un "filtre" est appliqué aux images au moment de leur construction pour régler certains problèmes de données dans l'algorithme de KNN. Le filtre a alors été choisi pour correspondre à une vidéo en noir et blanc.
La vidéo aura pour coordonnées le point le plus en bas à gauche spécifié au moment de l'appelle de la méthode.

### Construction d'un arbre L-System
L'arbre construit lors de l'appelle de la méthode correspondante est un sapin. Il est entièrement fait à l'aide de 2 L-Systems indépendant en commençant par générer un tronc composé de "A", "B" et "C".
Les "C" sont également ceux qui déclenchent la construction des branches avec une méthode privée en faisant appelle au second L-System composés de : "[",  "]", "/" et de "F". Les 2 premiers ont pour rôle de gérer une pile et servent à la construction de chaque branche indépendante (la pile permet de revenir à l'endroit précédent). Le "/" a pour rôle de changer la face de construction en changeant de point cardinal. Le "F" quant à lui a pour rôle de poser chaque block.

Le tronc a pour paramètres :
> axiom = "A"
> règles = {"A": "AB", "B": "AC"}
> itérations = itérations de l'utilisateur

Les branches ont pour paramètres :
> axiom = "A/A/A/A/A/A/A/A/A"
> règles = {"A": "[BBBB]", "B": "[F * valeur dépendant de la taille de l'arbre]"}
> itérations = 2

Les coordonnées de l'arbre représentent le centre du tronc au point le plus bas.

#### Info importante
La construction des branches de l'arbre est fortement inspiré de [cette](https://dev.minetest.net/L-system_tree_examples#Giant_dry_shrub) exemple de construction d'arbre.

### Construction d'une suite
L'appelle de la méthode de création d'une suite permet la construction d'un axe se construisant à -50 blocks en x par rapport aux coordonnées spécifiées jusqu'à +50 blocks en x pour créer l'axe des abscisses ainsi que la construction d'un axe en -50 blocks en y par rapport aux coordonnées jusqu'à + 50 blocks en y pour créer l'axe des ordonnées. Il y a aussi 2 flèches créées à +50 blocks en x et à +50 blocks en y. La suite est ensuite tracée.