voici les etapes pour l'exercise 4.2 ainsi que la donne necessaire (la donne se trouve aussi sur studium).

requirements
  -python
    -pandas
    -statsmodels

(lele, vu que ta aucune idee de c'est quoi, je vais te detailler comment installer python et le faire fonctionner sur ton ordi,
tu pouras toujours revenir voir ici comment faire si ten as besoin)

1: install ca -> https://code.visualstudio.com/      (c'est juste un editeur de code de base, comme word mais pour coder)

2: ouvre lapp sur ton ordi qui sappelle terminal et fait juste copier et coller la commande ci dessous, puis appuie sur enter pour l'executer
(on install brew pour installer git afin que tu puisse cloner mon code)

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

3: toujours dans le terminal, fais la meme chose pour ca
(maintenet, on install git comme mentionne plus haut. once again ca c'est juste pour que tu puisse copier mon code, ca a pas rapport avec le devoir en ten que tel)

brew install git

4: install ca -> https://www.python.org/downloads/
(le prof travail en R mais blc python c'est plus facile. on install python parce que ca prends un language de programmation pour faire ses trucs... aussi je connais pas R)

5: clone le repo (mon code) dans vscode.
  -ouvre vscode (que ta installer plus haut)
  -a gauche il ya plusieurs icone, clique sur la genre de branche avec 3 boules qui sappelle source control.
  -une fois dans source control, tu vas voir, en haut a droite, <<...>> (un icone de trois petits points), clique sur "clone" et choisi "from github" pui colle ca dedans
  <<https://github.com/gabrielderome/cost_benefit_ana.git>>
(bravo ta copier mon code!)

6: ouvre ton terminal encore once again et copy paste les 2 commandes
(install les librairies que jutilise pour le devoir dans ton python)

pip install pandas
pip install statsmodels

et la normalement on est good pour commencer le devoir XD -> tout ce que tas fait (ou pas) jusqua maintenent tas juste besoin de le faire une fois et ca vas te rendre la vie plus
facile pour les prochaines fois ou tauras besoin de copier mon code dans ce cours ou un autre.

pour le devoir en lui meme tu peux aller voir le script et les results dans le file qui fini par .py et si tu veux rouler les trucs toi
meme, un par un et voir ce que ca fait, tu peux aller rouler le "notebook", donc le file qui fini par .ipynb.

