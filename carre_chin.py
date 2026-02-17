# %%
import numpy as np

#Innitialiser la matrice à On,p
A = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

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
        A[i][j] = 1         # 1 est le symbole du joueur A par definition
        A[k][l] = -1        # -1 est le symbole du joueur B par définition
    condition_A = (np.diagonal(A) == [1, 1, 1]).all() or (np.diag(np.fliplr(A)) == [1, 1, 1]).all() or (A[:, 0] == [1, 1, 1]).all() or (A[:, 1] == [1, 1, 1]).all() or (A[:, 2] == [1, 1, 1]).all() or (A[0, :] == [1, 1, 1]).all() or (A[1, :] == [1, 1, 1]).all() or (A[2, :] == [1, 1, 1]).all()
    condition_B = (np.diagonal(A) == [-1, -1, -1]).all() or (np.diag(np.fliplr(A)) == [-1, -1, -1]).all() or (A[:, 1] == [-1, -1, -1]).all() or (A[1, :] == [-1, -1, -1]).all()
#Vérification et gagnants
if condition_A == True :
    print("Le joueur A a gagné le jeu")
    print(A)
if condition_B == True :
    print("Le joueur B a gagné le jeu")
    print(A)