import random
# la grille principale
# toutes les cases sont initialisées à 0
g = [[0] * 7 for _ in range(6)]
gvide = [[0] * 7 for _ in range(6)]
#grille d'affichage: toutes les cases sont initialisées au caractere .
grille_affiche = [["."] * 7 for _ in range(6)]
joueur1="X"
joueur2="O"
magrille_de_test= [[0] * 7 for _ in range(6)]
def clone_grille():
    for lig in range(6):
        for col in range(7):
            magrille_de_test[lig][col]=g[lig][col]


# la fonction retourne une grille vide où tous les cases sont à 0
def grille_vide():
	for lig in range(6):
		for col in range(7):
			g[lig][col]=0
	#puissance4_v2.affiche()
#	affiche()

def recommencer():
    grille_vide()
    print("voulez vous recommencer (O|o)?:")
    flag=input()
    if flag=="O" or flag=="o":
        return True
    else:
        return bool(False)


# cette fonction met à jour la grille_affiche à partir des valuers de la grille principale
# on met X lorsque la valeur de la case dans la grille principle est 1 et O lorsque la valuere est 2
def affiche():
	for ligne in range(6):
		for colonne in range(7):
			if g[ligne][colonne]==1:
				grille_affiche[ligne][colonne]=joueur1;
			elif g[ligne][colonne]==2:
					grille_affiche[ligne][colonne]=joueur2;
			else:
       			 grille_affiche[ligne][colonne]=".";
		print (str(grille_affiche[ligne]).replace(",","").replace("[","").replace("]","").replace("'",""));

def stocke_grille_ganante(joueur):
	fichier= open("gagant"+joueur,"a")

	for ligne in range(6):
		for colonne in range(7):
			if g[ligne][colonne]==1:
				grille_affiche[ligne][colonne]=joueur1;
			elif g[ligne][colonne]==2:
					grille_affiche[ligne][colonne]=joueur2;
			else:
       			 grille_affiche[ligne][colonne]=".";
		fichier.write(str(grille_affiche[ligne]).replace(",","").replace("[","").replace("]","").replace("'",""));
		fichier.write("\n")

# on verifie si il y'a une case de valeur 0 sur la ligne 0
def coup_possible(grille,c):
	retour = False;
	if grille[0][c]==0:
		retour = True;
	return retour;

# on commence par vérifier si la case de la ligne 0 et la colonne c est à 0.
# si c'est le cas alors on reverifie en repratant du bas (ligne 5) pour trouver la case ou la valeur est à 0 pour la remplacer par la valeur i




def jouer(grille,i,c):
	if i!=2 and i!=1:
		print ("joueur",i,"n existe pas")
		return True
	if coup_possible(grille,c):
		for ligne in reversed(range(6)):
			if grille[ligne][c]==0:
				grille[ligne][c]=i;
				return True;
	else:
		print("attention vous essayez de jouez une colonne pleine")
		return False


def coupGagnant(grille, joueur, ligne,colonne):
	#print ("coupGagnant(grille, joueur, ligne,colonne)",joueur, ligne,colonne)
	retour=bool(False)
	if horiz(grille, joueur, ligne,colonne)==True:
		retour=True
		if grille==g:
			print("le coup est gagant horizontalement pour le joueur",joueur)
		return retour
	elif vert(grille, joueur, ligne,colonne)==True:
		retour=True
		if grille==g:
			print("le coup est gagant verticalement pour le joueur",joueur)
		return retour
	elif diag(grille, joueur, ligne,colonne)==True:
		if grille==g:
			print("le coup est gagant diagonalement pour le joueur",joueur)
		retour=True
	return retour
	

def horizp(grille, joueur, ligne,colonne,position):
	retour=bool(False)
	if position==1 and colonne<4:
		if grille[ligne][colonne+1]==joueur and grille[ligne][colonne+2]==joueur and grille[ligne][colonne+3]==joueur:
			retour=True
		#print("horizp", joueur,ligne,colonne,position,retour)
	if position==2 and colonne<5 and colonne>0:
		if grille[ligne][colonne-1]==joueur and grille[ligne][colonne+1]==joueur and grille[ligne][colonne+2]==joueur:
			retour=True
		#print("horizp", joueur,ligne,colonne,position,retour)
	if position==3 and colonne<6 and colonne>1: 
		if grille[ligne][colonne-2]==joueur and grille[ligne][colonne-1]==joueur and grille[ligne][colonne+1]==joueur:
			retour=True
		#print("horizp", joueur,ligne,colonne,position,retour)
	if position==4 and colonne>2:
		if grille[ligne][colonne-3]==joueur and grille[ligne][colonne-2]==joueur and grille[ligne][colonne-1]==joueur:
			retour=True
		#print("horizp", joueur,ligne,colonne,position,retour)
	#print("horizp", ligne,colonne,joueur,retour)
	#if retour==True:
	#print("fin horizp", retour)
	return retour


def vertp(grille, joueur, ligne,colonne,position):
	retour = bool(False)
	#print ("debut vertp")
	if position==1 and ligne<3:
		retour=grille[ligne+1][colonne]==joueur and grille[ligne+2][colonne]==joueur and grille[ligne+3][colonne]==joueur
	if position==2 and ligne<4 and ligne>0:
		retour=grille[ligne-1][colonne]==joueur and grille[ligne+1][colonne]==joueur and grille[ligne+2][colonne]==joueur
	if position==3 and ligne<5 and ligne>1:
		retour=grille[ligne-2][colonne]==joueur and grille[ligne-1][colonne]==joueur and grille[ligne+1][colonne]==joueur
	if position==4 and ligne>2:
		retour=grille[ligne-3][colonne]==joueur and grille[ligne-2][colonne]==joueur and grille[ligne-1][colonne]==joueur
	#print("vertp", ligne,colonne,joueur,retour)

	return retour


def diagp(grille, joueur, ligne,colonne,position):
	retour=bool(False)
	retour1=bool(False)
	retour2=bool(False)
	try:
		retour1=grille[ligne][colonne]==joueur and grille[ligne+1][colonne+1]==joueur and grille[ligne+2][colonne+2]==joueur and grille[ligne+3][colonne+3]==joueur
	except:
		retour1=bool(False)
	try:

	#print("diagp(grille, joueur, ligne,colonne,position)",joueur,ligne,colonne,position)
	if position==1 and ligne<3 and colonne<4:
		#print ("if position==1 and [ligne<3 and colonne<4]",ligne,colonne)
		retour1=grille[ligne+1][colonne+1]==jou and grille[ligne+2][colonne+2]==joueur and grille[ligne+3][colonne+3]==joueur
	if position==1 and ligne<3 and colonne>2:
		retour2=grille[ligne+1][colonne-1]==joueur and grille[ligne+2][colonne-2]==joueur and grille[ligne+3][colonne-3]==joueur

	if position==2 and ligne<4 and colonne<5 :
		retour1=grille[ligne-1][colonne-1]==joueur and grille[ligne+1][colonne+1]==joueur and grille[ligne+2][colonne+2]==joueur
	if position==2 and ligne<4 and colonne<6 and colonne>1 :
		retour2=grille[ligne-1][colonne+1]==joueur and grille[ligne+1][colonne-1]==joueur and grille[ligne+2][colonne-2]==joueur
	

	if position==3 and ligne<5 and ligne>1 and colonne>1 and colonne<6:
		retour1=grille[ligne-2][colonne-2]==joueur and grille[ligne-1][colonne-1]==joueur and grille[ligne+1][colonne+1]==joueur
	if position==3 and ligne<5 and ligne>1 and colonne>0 and colonne<5:
		retour2=grille[ligne-2][colonne+2]==joueur and grille[ligne-1][colonne+1]==joueur and grille[ligne+1][colonne-1]==joueur


	if position==4 and ligne>2 and colonne>2:
		retour1=grille[ligne-3][colonne-3]==joueur and grille[ligne-2][colonne-2]==joueur and grille[ligne-1][colonne-1]==joueur
	if position==4 and ligne>2 and colonne<4:
		retour2=grille[ligne-3][colonne+3]==joueur and grille[ligne-2][colonne+2]==joueur and grille[ligne-1][colonne+1]==joueur

	if retour1 or retour2:
		retour=True
		#print ("diag gagant")
	return retour



def horiz(grille, joueur, ligne,colonne):
	retour=bool(False)
	for position in range(4):
		if bool(horizp(grille,joueur,ligne,colonne,position+1)):
			retour=bool(True)
			break
	return retour

def verifValeurColonne(c):
	retour=bool(False)
	try:
		if -1<int(c)<7:
			return True
		else:
			print("la valeur de la colonne doit etre un entier entre O et 6:")
			return False

	except:
		print("la valeur de la colonne doit etre un entier entre O et 6:")
		return False


def vert(grille, joueur, ligne,colonne):
	#print("debut vert")
	retour=bool(False)
	for position in range(4):
		if bool(vertp(grille, joueur, ligne,colonne,position+1)):
			retour=True
			break
	#print ("vert",retour)
	return retour


def diag(grille, joueur, ligne,colonne):
	#print("debut diag")
	retour=bool(False)
	for position in range(4):
		if bool(diagp(grille, joueur, ligne,colonne,position+1)):
			retour=True
			break
	#print ("fin diag",retour)
	return retour

def victoire(grille,joueur):
	retour=False
	for ligne in range(6):
		for colonne in range(7):
			if grille[ligne][colonne]==joueur:
				if coupGagnant(grille,joueur,ligne,colonne):
					return True
	#print("victoire",retour)
	return retour
def match_nul(grille):
	#print ("debut match_nul")
	retour=True
	for colonne in range(7):
		if coup_possible(g,colonne):
			retour=bool(False)
			break
	#print("fin match_nul",retour)
	if retour:
		print("attention match termine nul")
	return retour




def coup_aleatoire(grille,joueur):
	if match_nul(grille)==True:
		return
	colonne=random.randint(0, 6)
	bcolTrouve=False
	while bcolTrouve==False:
		if coup_possible(g,colonne):
			bcolTrouve=True
			jouer(g,joueur,colonne)
		else:
			colonne=random.randint(0, 6)

def coup_aleatoire_gagant(joueur): 
	retour=int(7)
	for colonne in range(7):
		clone_grille()
		if coup_possible(magrille_de_test,colonne):
			jouer(magrille_de_test,joueur,colonne)
			if victoire(magrille_de_test,joueur):
				retour=int(colonne)
				g
				break
	return retour

def get_colonne_ia(joueur): 
	retour=int(7)
	for colonne in range(7):
		clone_grille()
		if coup_possible(magrille_de_test,colonne):
			jouer(magrille_de_test,joueur,colonne)
			if victoire(magrille_de_test,joueur):
				retour=int(colonne)
				break
	return retour

def listeinclu(grille_travaille, grille_gagante):
	retour=True
	for ligne in range(6):

		for colonne in range(7):
			if grille_travaille[ligne][colonne]!=grille_gagante[ligne][colonne] and grille_travaille[ligne][colonne]!=".":
				retour=bool(False)
				return retour
				break
	return retour


def getColonneFromGrille(magrille,grille_contenante,joueur_de_comparaison):
	retour=int(7)
	if listeinclu(magrille,grille_contenante):
		for colonne in range(7):
			if magrille[0][colonne]==0 and grille_contenante[0][colonne]==joueur_de_comparaison:
				retour=colonne
				return retour
		for ligne in range(1,6):
			for colonne in range(7):
				if magrille[ligne-1][colonne]!=0 and magrille[ligne][colonne]==0 and grille_contenante[ligne][colonne]==joueur_de_comparaison:
					retour=int(colonne)
					#print("************la colonne est fournit par l IA***********")
					return retour
					break
			
	return retour


def grilles_from_file(fichier):
	grilles = []
	try:
		file=open(fichier,"r")
#	lines = reversed(file.readlines())
		lines1 = file.readlines()
		file.close()
		nombre_de_ligne=len(lines1)
		nombre_grille=int(nombre_de_ligne/6)
		#grilles=[[[0] * 7 for _ in range(6)] for _ in range(nombre_grille)]
		lines=[[0] * 7 for _ in range(nombre_de_ligne)]
		for item in range(nombre_de_ligne):
			lines[nombre_de_ligne-item-1]= lines1[item]
	#ligne=ligne1.reversed()
# fermez le fichier après avoir lu les lignes
	
	
	
		iteration=0
		while iteration < nombre_grille:
			grille_travaille = [[0] * 7 for _ in range(6)]
			for ligne in range(6):
				liste=lines[int(nombre_grille*6)-1-(6*iteration)-ligne].split()
				for colonne in range(7):
					if liste[colonne]=='.':
						grille_travaille[ligne][colonne]=0
					elif liste[colonne]=='O':
						grille_travaille[ligne][colonne]=2
					elif liste[colonne]=='X':
						grille_travaille[ligne][colonne]=1
			#print("on imprime la ligne",ligne,"de la grille",iteration+1)
			#print(grille_travaille[ligne])
			grilles.append(grille_travaille)
		#print("############# on a imprime la grille",iteration+1,"#####################")
			iteration +=1
	except:
		grilles=[]

	return grilles

