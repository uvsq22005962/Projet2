#########################################
# groupe  2 MPCI 6
# Cyril CLOVIS
# Dylan THUILLIER
# Ahmadou bamba SOUM
# Olivier GABRIEL
# https://github.com/uvsq22005256/projet_incendie
# https://discord.gg/fNQpuPM3yQ

#########################################
#Import des fonctions

import tkinter as tk 
import random as rd
import copy as cp

###############################################
#Variables 

global tableau, NB_COL, NB_LIG, COTE, compteur_clic, liste_sauvegarde, p, t, n, k

tableau = []
liste_sauvegarde = []
compteur_clic = 0

NB_COL = int(input("Veuillez saisir le nombre de colonnes: "))
NB_LIG = int(input("Veuillez saisir le nombre de lignes: "))
p = int(input("Veuillez définir la probabilité de case recouverte d'eau (en %): "))
n = int(input("Veuillez définir le nombre d'activation pour l'automate: "))
T = int(input("Veuillez définir le nombre minimum de cases voisines pour appliquer la règle: "))
k = int(input("Veuillez définir l'ordre: "))

COTE = 20

HAUTEUR = NB_LIG * COTE
LARGEUR = NB_COL * COTE


###############################################
#Fonctions

def grille():
    """La fonction crée la grille composé de carré marrons ou bleus avec les données fournies par l'utilisateur"""
    global i,j  #Pour y avoir acces dans les fonctions case_eau et case_terre
    for i in range(NB_COL):      #Pour comprendre cette fonction, essayez de dessiner le rectangle (0,0), (COTE,COTE). Puis le carreau suivant (COTE,COTE),(2*COTE,2*COTE)
        for j in range(NB_LIG):
            if pourcentage():     
                case_eau(i,j)
            else: 
                case_terre(i,j)           


def pourcentage():
    """La fonction attribue True ou False à chaque case, en fonction du pourcentage donné par l'utilisateur"""
    for nb in range(100):          #nb représente le "pour 100", en effet on le fait 100 fois
        nb = rd.randint(1,100)     # la nouvelle valeur de nb est donnée au hasard (nb est muet)
        if nb <= p:                # Pour 100 valeurs de nb fortuites on regarde lesquelles sont inferieurs à la probabilité (donc lesquelles respectent la probablité)
            return True
        else: 
            return False
    

def case_eau(a,b):       #a pour i (colonnes) et b pour j (lignes)
    """Cree la case de coordonées a,b et lie la liste
       avec le canvas en lui associant la couleur bleu 
       sur le canvas et le chiffre 1 dans la liste"""
    x, y = a*COTE, b*COTE
    tableau[a][b] = 1    #1 correspond à bleu donc l'eau
    color = "blue"
    carreau_blue = canvas.create_rectangle((x, y),(x+COTE, y+COTE), fill=color)
    return carreau_blue


def case_terre(a,b):
    """Cree la case de coordonées a,b, et lie la liste
       avec le canvas en lui associant la couleur marron sur le 
       canvas et le chiffre 0 dans la liste"""
    x, y = a*COTE, b*COTE
    tableau[a][b] = 0   #0 correspond à marron donc la terre
    color = "brown"
    carreau_marron = canvas.create_rectangle((x, y),(x+COTE, y+COTE), fill=color)
    return carreau_marron


def nb_case_eau(a, b):
    """Retourne le nombre de cases bleus (recouverte d'eau)
       autour de la case de coordonnées (i, j)"""
    cpt = 0
    for y in range(max(0, a-k), min(NB_COL,(a+k)+1)):                #si k=1, a-1 < a < a+1 (ordre 1, comme jeu de la vie)
        for z in range(max(0, b-k), min(NB_LIG, (b+k)+1)):            
            if tableau_memoire[y][z] == 1 and [y, z] != [a, b]:   #(mais dans les 4 coins a-1 ou a+1 n'existent pas )
                cpt += 1
    return cpt

def conversion(a,b):
    """Recueille la valeur du voisinnage défini par l'utilisateur et 
       la compare avec le nombre de case recouverte d'eau pour agir en conséquence
       avec la fonction case_eau ou case_terre"""
    nb_eau = nb_case_eau(a, b)
    if nb_eau >= T:
        case_eau(a,b)
    else:
        case_terre(a,b)

def etape():
    global tableau_memoire
    """Copie le tableau initial afin de faire une étape de conversion toutes les
     cases du canvas, sans etre influencé par les conversions précédentes."""
    #ATTENTION, ici la conversion(i,j) modifie le tableau. Ainsi, on ne peut pas prendre ce tableau 
    #pour les étapes car les valeurs de ce tableau changent à chaque étape sur une case. Donc un changement
    #sur une case n, fausserait la conversion pour la case n+1, d'ou le tableau_memoire qui reste intact malgré
    # les conversions(seul tableau est modfié), ensuite on récupère toutes les valeurs modifié dans le tableau_mémoire
    tableau_memoire = cp.deepcopy(tableau)
    for i in range(NB_COL):
        for j in range(NB_LIG):
            conversion(i,j)
    tableau_memoire = tableau  
    return tableau_memoire
    

def nombre_etape():
    """Réalise n fois la fonction étape, avec n donné par l'utilisateur"""
    compte_n = 0
    while compte_n <= n:
        compte_n += 1
        etape()


def personnage(event):
    """Creer le personnage sur une case terre, là ou l'utilisateur à cliqué 
       et renvoie ses coordonnées sinon, la fonction supprime le personnage"""
    global compteur_clic, perso, tableau_memoire, x0 , y0 , x1 , y1, a, b
    a,b = event.x // COTE, event.y // COTE
    x, y = a*COTE, b*COTE
    if compteur_clic % 2 == 0:
        if tableau_memoire[a][b] == 0:     #doit se poser sur la terre
            compteur_clic += 1
            perso = canvas.create_rectangle((x, y),(x+COTE, y+COTE), fill="red")     
            x0 , y0 , x1 , y1 = canvas.coords(perso)
            return x0 , y0 , x1 , y1
    else:
        canvas.delete(perso)
        compteur_clic += 1


def verifie_droite(abscisse0, abscisse1):   
    """Renvoie True si le maximum des abscisses est inférieur à la LARGEUR"""
    return max(abscisse0, abscisse1) < LARGEUR


def verifie_gauche(abscisse0, abscisse1):  
    """Renvoie True si le minimum des abscisses est supérieur à 0""" 
    return 0 < min(abscisse0, abscisse1)


def verifie_haut(ordonnée0, ordonnée1):   
    """Renvoie True si le minimum des ordonnées est supérieur à 0""" 
    return 0 < min(ordonnée0, ordonnée1)


def verifie_bas(ordonnée0, ordonnée1):   
    """Renvoie True si le maximum des ordonnées est inférieur à la HAUTEUR""" 
    return max(ordonnée0, ordonnée1) < HAUTEUR


def verifie_case(a,b):
    """Etudie l'état de la case de coordonnées a,b et renvoie True
       si la case étudié est de la terre (corespond à 0) """
    nv_compteur = 0         
    if tableau_memoire[a][b] == 1:  
        nv_compteur += 1
    if nv_compteur == 0:
        return True


def droite(event):
    """Permet ou pas le déplacement du personnage vers la 
       droite et appelle la fonction sauvegarde, lorsque l'utilisateur
       clique sur la flèche de droite"""
    global perso, x0, y0 , x1 , y1 
    i, j = int(x0// COTE), int(y0// COTE)
    if verifie_droite(x0,x1) and verifie_case(i+1,j):
        canvas.move(perso,COTE,0) 
        x0 , y0 , x1 , y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        return  x0 , y0 , x1 , y1
    else:
        pass


def gauche(event):
    """Permet ou pas le déplacement du personnage vers la 
       gauche et appelle la fonction sauvegarde, lorsque l'utilisateur
       clique sur la flèche de gauche"""
    global perso, x0, y0 , x1 , y1 
    i, j = int(x0// COTE), int(y0// COTE)
    if verifie_gauche(x0,x1) and verifie_case(i-1,j):
        canvas.move(perso,-COTE,0) 
        x0 , y0 , x1 , y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        return  x0 , y0 , x1 , y1
    else:
        pass

 
def haut(event):
    """Permet ou pas le déplacement du personnage vers le 
       haut et appelle la fonction sauvegarde, lorsque l'utilisateur
       clique sur la flèche du haut"""
    global perso, x0, y0 , x1 , y1 
    i, j = int(x0// COTE), int(y0// COTE)
    if verifie_haut(y0,y1) and verifie_case(i, j-1):
        canvas.move(perso,0,-COTE) 
        x0 , y0 , x1 , y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        return  x0 , y0 , x1 , y1
    else:
        pass


def bas(event):
    """Permet ou pas le déplacement du personnage vers le 
       bas et appelle la fonction sauvegarde, lorsque l'utilisateur
       clique sur la flèche du bas"""
    global perso, x0, y0 , x1 , y1 
    i, j = int(x0// COTE), int(y0// COTE)
    if verifie_bas(y0,y1) and verifie_case(i, j+1):
        canvas.move(perso,0,COTE) 
        x0 , y0 , x1 , y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        return  x0 , y0 , x1 , y1
    else:
        pass


def sauvegarde_deplacement():
    """Ajoute dans la liste_sauvegarde les coordonnées occupées
       sucessivement par le personnagge"""
    global liste_sauvegarde
    liste_sauvegarde.append(canvas.coords(perso))
    return liste_sauvegarde


def annuler(event):
    """Si la liste n'est pas vide, annuler permet à 
       l'utilisateur de revenir à la dernière position occupé
       avant son avant son déplacement """
    global x0 , y0 , x1 , y1, perso, liste_sauvegarde
    if liste_sauvegarde != [] :
        x0 , y0 , x1 , y1 = liste_sauvegarde[-2]
        canvas.coords(perso, x0 , y0 , x1 , y1)
        del liste_sauvegarde[-2]
    else: 
        pass
    
def sauvegarder():
    pass

def charger():
    pass

###############################################
#Programme principal

for i in range(NB_COL):
    tableau.append([0] * NB_LIG)


racine = tk.Tk()
racine.title("Terrain de jeu")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
bout_sauv = tk.Button(racine, text="Sauvegarder", command=sauvegarder)
bout_charger = tk.Button(racine, text="Charger", command=charger)
grille()
nombre_etape()
racine.bind("<1>", personnage)
racine.bind("<Right>", droite)
racine.bind("<Left>", gauche)
racine.bind("<Up>", haut)
racine.bind("<Down>", bas)
racine.bind("<Return>", annuler) # touche entrée

canvas.grid(columnspan=3)
bout_sauv.grid(column=0, row=1)
bout_charger.grid(column=2, row=1)

racine.mainloop()


