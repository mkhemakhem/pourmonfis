import puissance4_v2
import grilles as gr
import puissance4_grille_ia as ia
import random


def main():
    matchFini = False
    iteration = 0
    JoueurSuivant = random.randint(1, 2)
    while (matchFini == False):
        iteration = iteration+1
        print("Joueur encours", JoueurSuivant)
        if JoueurSuivant == 2:
            colonne_gagant = int(
                puissance4_v2.coup_aleatoire_gagant(JoueurSuivant))
            if colonne_gagant == 7:
                colonne_gagant_adversaire = int(
                    puissance4_v2.coup_aleatoire_gagant(1))
                if colonne_gagant_adversaire == 7:
                    if iteration > 2:
                       
                        colonne_ajouer = 7
                        grilles = gr.grilles_from_file(2)
                        for grille in grilles:
                            if ia.isIncluded(puissance4_v2.g, grille) == True:
                                colonne_ajouer = ia.getColonne(puissance4_v2.g,grille, 2)
                                puissance4_v2.jouer(puissance4_v2.g, JoueurSuivant, colonne_ajouer)
                                break
                        if colonne_ajouer == 7:
                            grilles = gr.grilles_from_file(1)
                            for grille in grilles:
                                if ia.isIncluded(puissance4_v2.g, grille) == True:
                                    colonne_ajouer = ia.getColonne(puissance4_v2.g,grille, 1)
                                    puissance4_v2.jouer(
                                           puissance4_v2.g, JoueurSuivant, colonne_ajouer)
                                    break
                            if colonne_ajouer == 7:
                                puissance4_v2.coup_aleatoire(
                                   puissance4_v2.g, JoueurSuivant)
                    else:
                        puissance4_v2.coup_aleatoire(
                                   puissance4_v2.g, JoueurSuivant)
                        
                else:
                    # on empeche l'adversaire de gagner
                    puissance4_v2.jouer(
                          puissance4_v2.g, JoueurSuivant, colonne_gagant_adversaire)
            else:
                puissance4_v2.jouer(
                    puissance4_v2.g, JoueurSuivant, colonne_gagant)

        else:
            print("entrer un choix de colonne")
            bonchoix = 7
            while bonchoix == 7:
                try:
                    colonne = int(input())
                    if colonne <0 or colonne>6:
                        print("votre choix doit etre un entier entre 0 et 6")
                        bonchoix=7
                        
                    else:
                        if puissance4_v2.jouer(puissance4_v2.g, 1, colonne):
                            bonchoix = colonne
                except:
                    print ("votre choix doit etre un entier entre 0 et 6")
                    bonchoix=7

        puissance4_v2.affiche()
        tag1 = puissance4_v2.victoire(puissance4_v2.g, JoueurSuivant)
        if tag1 == True:
            gr.stocke_grille_ganante(puissance4_v2.g,JoueurSuivant)
        tag2 = puissance4_v2.match_nul(puissance4_v2.g)

        if tag1 == True or tag2 == True:
            iteration=0

            if puissance4_v2.recommencer():
                main()
            else:
                matchFini = True

        if JoueurSuivant == 1:
            JoueurSuivant = 2
        else:
            JoueurSuivant = 1


main()
