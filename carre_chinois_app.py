import streamlit as st
import numpy as np


st.header("Carré Chinois")

# Initialisation de la table et du pion du joueur 
if "board" not in st.session_state:
    st.session_state.board = np.full((3,3), "")

if "player" not in st.session_state:
    st.session_state.player = "X"
    
#On initialise les conditions de victoire des joueurs
if "game_over" not in st.session_state:
    st.session_state.game_over = False

#Compteur pour x (Joueur A)
if "counter_x" not in st.session_state:
    st.session_state.counter_x = 0

#Compteur pour y (Joueur B)
if "counter_o" not in st.session_state:
    st.session_state.counter_o = 0

#Changer de joueur en fonction du pion
if st.session_state.player == "X":
    Joueur_actuel = "Joueur A"
else:
    Joueur_actuel = "Joueur B"
st.write(f"Joueur actuel : {Joueur_actuel}")

#Création de la fonction qui vérifie qui a gagné
def check_winner(M)-> bool:
    for i in range(3):
        if all(M[i, :] == M[i, 0]) and M[i, 0] != "":
            return True
        if all(M[:, i] == M[0, i]) and M[0, i] != "":
            return True
    if all(np.diag(M) == M[0, 0]) and M[0, 0] != "":
        return True
    if all(np.diag(np.fliplr(M)) == M[0, 2]) and M[0, 2] != "":
        return True
    return False

# Création de la grille
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        if cols[j].button(st.session_state.board[i][j] or " ", key=f"{i}{j}"):
            if not st.session_state.game_over and st.session_state.board[i][j] == "":
                st.session_state.board[i][j] = st.session_state.player
                if check_winner(st.session_state.board) == True:
                    @st.dialog("Vainqueur 🎉")
                    def show_dialog():
                        st.success(f"🎊 {Joueur_actuel} a gagné !")
                        #Boutton pour recommencer le jeu
                        Restart = st.button("Reprendre le jeu")
                        if Restart:
                            st.session_state.board = np.full((3, 3), "")
                            st.session_state.player = "X"
                            st.session_state.game_over = False
                            st.rerun()
                    show_dialog()
                else:
                    # Changer de joueur
                    if st.session_state.player == "X":
                        st.session_state.player = "O"
                    else:
                        st.session_state.player = "X"

# Affichage tableau
st.write("Plateau actuel :")
st.write(st.session_state.board)

#Boutton pour recommencer le jeu
Restart = st.button("Reprendre le jeu")
if Restart:
    st.session_state.board = np.full((3, 3), "")
    st.session_state.player = "X"
    st.session_state.game_over = False