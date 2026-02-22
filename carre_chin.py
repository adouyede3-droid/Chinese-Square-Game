# %%
import numpy as np

#Innitialiser la matrice vide
A = np.full((3, 3), "", dtype=object)

# %%
#Critère de victoire du joueur A
condition_A = False

#Critère de victoire du joueur B
condition_B = False

#Lancement du jeu
while (not condition_A) and (not condition_B):
    i = int(input("Joueur A entrer la ligne de votre pion"))
    j = int(input("Joueur A entrez maintenant le numéro de la colonne de votre pion"))
    k = int(input("Joueur B entrez la ligne de votre pion"))
    l = int(input("Joueur B entrez maintenant le numéro de la colonne de votre pion"))
    if (i, j) != (k, l):
        A[i][j] = "X"         # X est le symbole du joueur A par definition
        A[k][l] = "O"        # O est le symbole du joueur B par définition
    condition_A = (np.diagonal(A) == ["X", "X", "X"]).all() or (np.diag(np.fliplr(A)) == ["X", "X", "X"]).all() or (A[:, 0] == ["X", "X", "X"]).all() or (A[:, 1] == ["X", "X", "X"]).all() or (A[:, 2] == ["X", "X", "X"]).all() or (A[0, :] == ["X", "X", "X"]).all() or (A[1, :] == ["X", "X", "X"]).all() or (A[2, :] == ["X", "X", "X"]).all()
    condition_B = (np.diagonal(A) == ["O", "O", "O"]).all() or (np.diag(np.fliplr(A)) == ["O", "O", "O"]).all() or (A[:, 1] == ["O", "O", "O"]).all() or (A[1, :] == ["O", "O", "O"]).all()
#Vérification et gagnants
if condition_A == True :
    print("Le joueur A a gagné le jeu")
    print(A)
if condition_B == True :
    print("Le joueur B a gagné le jeu")
    print(A)
