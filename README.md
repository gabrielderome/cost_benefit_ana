# Instructions pour l'exercice 4.2

Voici les étapes à suivre pour réaliser l'exercice 4.2, ainsi que les fichiers nécessaires (les données se trouvent aussi sur Studium).

## Pré-requis

Python
  -pandas
  -statsmodels


(Lele, comme tu n’as jamais programmé, je vais t’expliquer en détail comment installer Python et le faire fonctionner sur ton ordi. N’hésite pas à revenir ici si tu es bloquée à un moment donné.)

## Étapes pour installer tout ce que tas besoin
### Installe Visual Studio Code
-> Télécharge-le ici. "https://code.visualstudio.com/"
(C'est juste un éditeur de code, un peu comme Word, mais pour coder.)

### installe homebrew
Ouvre le terminal sur ton ordi et copie-colle la commande ci-dessous, puis appuie sur "Entrée".
(On va installer Homebrew, un outil qui permet d'installer d'autres logiciels, comme Git, dont tu as besoin pour récupérer mon code.)

```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

### Installe Git
(Toujours dans le terminal, copie et colle cette commande, puis appuie sur "Entrée". Git te permet de cloner (copier) mon code.)

```brew install git```

### Installe Python
-> Télécharge-le ici. "https://www.python.org/downloads/"

(Le prof utilise R, mais on va travailler avec Python parce que c’est plus simple et je le maîtrise mieux.)
### Clone mon repo dans VS Code
-Ouvre Visual Studio Code.

-À gauche, tu verras plusieurs icônes. Clique sur celle qui ressemble à une branche avec trois points (c’est "Source Control").

-En haut à droite, clique sur les trois petits points ("..."), puis sur "Clone". Choisis "From GitHub" et colle ce lien:
"https://github.com/gabrielderome/cost_benefit_ana.git"

(Bravo, tu as copié mon code sur ton ordi !)

### Installe les librairies nécessaires
(Toujours dans le terminal, copie-colle ces deux commandes pour installer les librairies dont on a besoin pour le devoir.)

```pip install pandas```

```pip install statsmodels```

si ca marche pas, essaye

```pip3 install pandas```

```pip3 install statsmodels```

Et voilà, normalement tu es prête à commencer ! Tout ce que tu viens de faire, c’est à faire une seule fois, et ça te facilitera la vie pour les autres devoirs ou exercices.

## Pour le devoir en lui-même :
Tu peux regarder le script et les résultats dans le fichier qui se termine par .py.

Si tu veux exécuter toi-même les différentes étapes, tu peux ouvrir le fichier .ipynb (notebook) et voir les résultats au fur et à mesure.

J’espère que ça te sera utile ! N’hésite pas si tu as des questions, je suis là pour t’aider 😄.
