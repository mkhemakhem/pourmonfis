import puissance4_v2
import grilles as gr
import puissance4_grille_ia as ia
import random


def jouer(demarrage):
    matchFini = False
    iteration=0
    JoueurEncours = random.randint(1, 2)
    if JoueurEncours==1:
        JoueurEnAttente=2
    else:
       JoueurEnAttente=1
        
    while (matchFini == False):
        iteration = iteration+1
        print("Joueur encours", JoueurEncours)
        if 2 == 2:
            colonne_gagant = int(
                puissance4_v2.coup_aleatoire_gagant(JoueurEncours))
            if colonne_gagant == 7:
                colonne_gagant_adversaire = int(
                    puissance4_v2.coup_aleatoire_gagant(JoueurEnAttente))
                if colonne_gagant_adversaire == 7:
                    if iteration > int(demarrage):
                       
                        colonne_ajouer = 7
                        grilles = gr.grilles_from_file(JoueurEncours)
                        for grille in grilles:
                            if ia.isIncluded(puissance4_v2.g, grille) == True:
                                colonne_ajouer = ia.getColonne(puissance4_v2.g,grille, JoueurEncours)
                                try:
                                    puissance4_v2.jouer(puissance4_v2.g, JoueurEncours, colonne_ajouer)
                                    break
                                except:
                                    print("pas de colonne retournee malgres que la grille est inclue")
                        if colonne_ajouer == 7:
                            grilles = gr.grilles_from_file(JoueurEnAttente)
                            for grille in grilles:
                                if ia.isIncluded(puissance4_v2.g, grille) == True:
                                    colonne_ajouer = ia.getColonne(puissance4_v2.g,grille,JoueurEnAttente)
                                    try:
                                        puissance4_v2.jouer(puissance4_v2.g, JoueurEncours, colonne_ajouer)
                                        break
                                    except:
                                        print("pas de colonne retournee malgres que la grille est inclue adverse")
                                        
                            if colonne_ajouer == 7:
                                puissance4_v2.coup_aleatoire(
                                   puissance4_v2.g, JoueurEncours)
                    else:
                        puissance4_v2.coup_aleatoire(
                                   puissance4_v2.g, JoueurEncours)
                        
                else:
                    # on empeche l'adversaire de gagner
                    puissance4_v2.jouer(
                          puissance4_v2.g, JoueurEncours, colonne_gagant_adversaire)
            else:
                puissance4_v2.jouer(
                    puissance4_v2.g, JoueurEncours, colonne_gagant)

        
        puissance4_v2.affiche()
        tag1 = puissance4_v2.victoire(puissance4_v2.g, JoueurEncours)
        if tag1 == True:
            gr.stocke_grille_ganante(puissance4_v2.g,JoueurEncours)
        tag2 = puissance4_v2.match_nul(puissance4_v2.g)

        if tag1 == True or tag2 == True:
            iteration=0
            matchFini=True
            puissance4_v2.grille_vide()


        if JoueurEncours == 1:
            JoueurEncours = 2
            JoueurEnAttente=1
        else:
            JoueurEncours = 1
            JoueurEnAttente=2


def main():
    for repetition in range(10000):
        jouer(1)
        
main()