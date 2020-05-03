def isIncluded(g_jeu,g_ia):
    for ligne in reversed(range(6)):
        for colonne in range(7):
            if g_jeu[ligne][colonne]!=0 and g_jeu[ligne][colonne]!=g_ia[ligne][colonne]:
                return False
                break
    return True
#cette fonction à partir d'une grille temoin dans la quelle grille de jeu est inclu, 
#elle retourne le numero de colonne joueable est qui a la valeur du joueur de la grille temoin
def getColonne(g_jeu,g_ia,joueur):
    for ligne in reversed(range(6)):
        for colonne in range(7):
            if g_jeu[ligne][colonne]==0 and g_jeu[ligne][colonne]==joueur:
                return colonne
                break
