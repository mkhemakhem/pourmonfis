fichier_grille_gagnant = "data/gagant"
extension = ".data"


def grilles_from_file(joueur):
    grilles = []
    fichier = fichier_grille_gagnant+joueur+extension
    try:
		file = open(fichier, "r")
#	lines = reversed(file.readlines())
		lines1 = file.readlines()
		file.close()
		nombre_de_ligne = len(lines1)
		nombre_grille = int(nombre_de_ligne/6)
		# grilles=[[[0] * 7 for _ in range(6)] for _ in range(nombre_grille)]
		lines = [[0] * 7 for _ in range(nombre_de_ligne)]
		for item in range(nombre_de_ligne):
			lines[nombre_de_ligne-item-1] = lines1[item]
	# ligne=ligne1.reversed()
# fermez le fichier après avoir lu les lignes

		iteration = 0
		while iteration < nombre_grille:
			grille_travaille = [[0] * 7 for _ in range(6)]
			for ligne in range(6):
				liste = lines[int(nombre_grille*6)-1-(6*iteration)-ligne].split()
				for colonne in range(7):
					if liste[colonne] == '.':
						grille_travaille[ligne][colonne] = 0
					elif liste[colonne] == 'O':
						grille_travaille[ligne][colonne] = 2
					elif liste[colonne] == 'X':
						grille_travaille[ligne][colonne] = 1
			# print("on imprime la ligne",ligne,"de la grille",iteration+1)
			# print(grille_travaille[ligne])
			grilles.append(grille_travaille)
		# print("############# on a imprime la grille",iteration+1,"#####################")
			iteration += 1
    except:
		grilles=[]

    return grilles
