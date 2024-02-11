# Minetest Museum
## Lancer le projet
### Installation de la librairie nécessaire
Le projet utilise la librairie [```moviepy```](https://pypi.org/project/moviepy/) pour lire une vidéo et la manipuler. Il est alors nécessaire de l'installer pour pouvoir exécuter le programme.
Pour cela il faut exécuter la commande :
```pip install moviepy```
Ou alors l'installer à l'aide du fichier requirement.txt présent dans le projet avec la commande en se plaçant dans le même dossier que le fichier :
```pip install requirement.txt```
Il est également possible d'installer cette librairie directement via l'IDE PyCharm depuis le menu ```Python Packages```.
### Lancer le projet
Il y a 2 manières de lancer le projet :
- La première est depuis le fichier ```main.py``` qui fera alors apparaitre plusieurs créations proche du 0 200 0 (à cause d'un bug de Pycraft faisant que tous les blocks ne se placent pas, je suis obligé de répéter la création de certaines créations ce qui peut prendre du temps sans pour autant garantir que tous les blocks se sont correctement placés, dans mon cas il me faut 6 min le temps d'afficher toutes les images [le reste est rapide])
- La seconde est depuis le fichier ```app.py``` qui contient une application graphique faite à l'aide de Tkinter qui permettra de faire apparaitre n'importe quoi à n'importe quelles coordonnées ainsi que de sélectionner le paramètre K du KNN (à 8 par défaut si on le lance de l'autre manière, normalement le résultat renvoyé par la méthode)

## Type de constructions
Le projet comporte 5 types de constructions différents, l'image, le L-System, la vidéo, l'arbre et la suite.
### Construction d'une image
La construction d'une image comporte 3 variantes différentes symbolisés par 3 méthodes de la classe ```MinetestMuseum``` différentes qui sont :
- ```draw_image_2d``` permettant la construction d'une image en 2 dimensions
- ```draw_image_minor_3d``` permettant la construction d'une image en 3 dimensions utilisant le principe de grayscale et de colonnes
- ```draw_image_full_3d``` permettant la construction d'une image en 3 dimensions utilisant à la fois le grayscale et les colonnes mais aussi les L-System
L'image aura pour coordonnées le point le plus en bas à gauche spécifié au moment de l'appelle de la méthode.
Il arrive que si l'image est trop grande une partie soit coupée, il suffit dans ce cas de la relancer pour obtenir les morceaux manquant.

### Construction d'une structure simple de L-System
Cette structure bien que pouvant être construit indépendamment est principalement faite pour être utilisé pour la création d'images 3d cependant il est possible d'y gérer les règles élémentaires d'un L-System c'est à dire l'axiom, les règles et l'itérations. 
Les structures choisies lors de la génération d'image ont ces paramètres :
> axiom = "A"
> règles = {"A": "AB", "B": "A"}
> itérations = grayscale // 100

### Construction d'une vidéo
Les vidéos choisies doivent de préférence être en noir et blanc puisqu'un "filtre" est appliqué aux images au moment de leur construction pour régler certains problèmes de données dans l'algorithme de KNN. Le filtre a alors été choisi pour correspondre à une vidéo en noir et blanc.
La vidéo aura pour coordonnées le point le plus en bas à gauche spécifié au moment de l'appelle de la méthode.
Malheureusement même en optimisant il a été impossible d'avoir une vidéo fluide, la vidéo doit être 1 FPS mais ne doit finalement qu'être affiché à environ 0,75. Pour régler ce problème on pourrait peut-être essayer d'utiliser la fonction de Pycraft pour placer plusieurs blocks à la fois et si elle est plus rapide que celle place block par block alors peut-être nous pourrions obtenir une vidéo fluide.

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
Comme l'image, il arrive que si l'itération est trop importante certains blocks ne se placent pas, il suffit de le relancer.

L'itération minimale est à 5 puisque en dessous l'arbre n'est qu'un tronc sans branche. J'ai donc décidé de mettre une itération minimale pour avoir un résultat minimum.

#### Info importante
La construction des branches de l'arbre est fortement inspiré de [cette](https://dev.minetest.net/L-system_tree_examples#Giant_dry_shrub) exemple de construction d'arbre.

### Construction d'une suite
L'appelle de la méthode de création d'une suite permet la construction d'un axe se construisant à -50 blocks en x  jusqu'à +50 blocks en x pour créer l'axe des abscisses ainsi que la construction d'un axe en -50 blocks en y jusqu'à + 50 blocks en y pour créer l'axe des ordonnées. Il y a aussi 2 flèches créées à +50 blocks en x et à +50 blocks en y. La suite est ensuite tracée.

## Idées d'améliorations
Il pourrait y avoir plusieurs idées pour améliorer le concept. Je pourrais par exemple jouer le son en même temps que la vidéo, dessiner des fonctions, avoir un système d'orientation qui faciliterait le placement, pouvoir modifier dans certains formats les images et vidéos pour être plus libre de la taille de ces derniers ou encore téléporter l'utilisateur pour qu'il soit dans le meilleur angle possible pour voir la création. Il est également probable qu'en utilisant le multi-threading j'aurais pu améliorer le mouvement de la vidéo. Je pourrai aussi ajouter une Entry à ma fenêtre Tkinter au niveau des suites pour pouvoir y rentrer la suite à tracer facilement.

#### Lien Github du projet [ici](https://github.com/flastar-fr/minetest)