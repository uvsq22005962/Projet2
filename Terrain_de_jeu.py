#########################################
# groupe  2 MPCI 6
# Cyril CLOVIS
# Dylan THUILLIER
# Ahmadou bamba SOUM
# Olivier GABRIEL
# https://github.com/uvsq22005256/projet_incendie
# https://discord.gg/fNQpuPM3yQ

#########################################
# Import des fonctions

import copy as cp
import random as rd
import tkinter as tk

###############################################
# Variables

compteur_formulaire = 0
tableau = []
liste_sauvegarde = []
liste_transition = []
compteur_clic = 0
liste_touche = ["Début"]
perso = []
NB_COL = 50
NB_LIG = 50
P = 50
T = 5
N = 4
K = 1
COTE = 20
HAUTEUR = NB_LIG * COTE
LARGEUR = NB_COL * COTE

###############################################
# Fonctions


def formulaire():
    """Gère la gestion de l'interface en appelant la fonction recueille_donne

    pour l'ensemble des paramètres. Elle organise donc l'interface en 15
    boutons, 6 entrées et 6 labels.
    """ 
    recueille_donne(" nombres de colonnes (par défaut: 50)",
                    NB_COL, 2, 1, 2, 3)
    recueille_donne(" nombres de lignes (par défaut: 50)",
                    NB_LIG, 4, 4, 5, 6)
    recueille_donne(" la probabilité de case recouverte d'eau en %,"
                    "(par défaut: 50)", P, 6, 7, 8, 9)
    recueille_donne(" le nombre minimum de cases voisines pour appliquer"
                    "la règle (par défaut: 5)", T, 8, 10, 11, 12)
    recueille_donne(" le nombre d'activation pour l'automate"
                    "(par défaut: 4)", N, 10, 13, 14, 15)
    recueille_donne(" l'ordre (par défaut: 1)", K, 12, 16, 17, 18)


def recueille_donne(information, valeur, placement, entree, defaut, valide):
    """Donne quelques consignes à l'utilisateur en créeant 2 labels.Puis,
    
    gère la création et le placement des entrées et des labels en prenant
    en paramètre l'information, la valeur associé et le placement.De plus,
    les paramètres defaut et valide permettent de créer les boutons Valider
    et Défaut et de les associer à leur entrées respectives. Enfin, crée
    et place les boutons désactivés bout_terrain, bout_sauv et bout_charger.
    """
    global bout_terrain, bout_sauv, bout_charger
    mode_emploi = tk.Label(racine, text="Vous devez impérativement rentrer"
                        "les valeurs en suivant l'ordre de placement des"
                        "boutons.\nVous devez donc remplir le tableau de"
                        "gauche à droite et de haut en bas.")
    mode_emploi.grid(column=0, row=0)
    mode_emploi2 = tk.Label(racine, text="Lorsque vous avez rentré votre"
                            "valeur, validez là DIRECTEMENT après.\n Si"
                            " vous voulez préserver la valeur par défaut,"
                            "cliquez directement sur le boutton :défaut.")
    mode_emploi2.grid(column=0, row=1)
    indication = tk.Label(racine, text="Veuillez saisir"+information)
    indication.grid(column=0, row=placement)
    entree = tk.Entry(racine, width=10)
    entree.grid(column=0, row=placement+1)
    defaut = tk.Button(racine, text="Défaut",
                                command=lambda:recuperation(valeur,
                                entree, defaut, valide, "défaut"))
    defaut.grid(column=1, row=placement+1)
    valide = tk.Button(racine, text="Valider",
                                command=lambda:recuperation(valeur,
                                entree, defaut, valide, "valider"))
    valide.grid(column=2, row=placement+1)
    bout_terrain = tk.Button(racine,
                            text="Lancement génération terrain de jeu",
                            command=lancement_terrain,
                            state="disabled")
    bout_terrain.grid(column=0, row=14)
    bout_sauv = tk.Button(racine, text="Sauvegarder",
                        command=sauvegarder_terrain,state="disabled")
    bout_sauv.grid(column=0, row=15)
    bout_charger = tk.Button(racine, text="Charger",
                    command=charger_terrain, state="disabled")
    bout_charger.grid(column=0, row=16)


def recuperation(valeur, entree, defaut, valide, choix):
    """Récupère la valeur entrée par l'utilisateur depuis l'interface puis

    désactive les boutons Défaut, Valider et l'entrée correspondants. Enfin,
    elle appelle la fonction liste.
    """
    global compteur_formulaire
    if choix == "valider":
        valeur = entree.get()
    entree.config(state="disabled")
    defaut.config(state="disabled")
    valide.config(state="disabled")
    compteur_formulaire += 1
    valeur = int(float(valeur))
    liste(valeur)


def liste(v):
    """Si le nombre de clic est inférieur ou égale à 6, la fonction ajoute
    
    la valeur passé en paramètre dans une liste. Au sixième clique, active
    le boutton: bout_terrain.Lorsque le compteur atteint 7, la liste
    attribue les valeurs à  NB_COL, NB_LIG, p, T, n, k et renvoie True.
    """
    global NB_COL, NB_LIG, P, T, N, K, HAUTEUR, LARGEUR
    if compteur_formulaire <= 6:
        liste_transition.append(v)
    if compteur_formulaire == 6:
        bout_terrain.config(state="normal")
    elif compteur_formulaire == 7:
        NB_COL = liste_transition[0]
        NB_LIG = liste_transition[1]
        P = liste_transition[2]
        T = liste_transition[3]
        N = liste_transition[4]
        K = liste_transition[5]
        HAUTEUR = NB_LIG * COTE
        LARGEUR = NB_COL * COTE
        return True

    
def lancement_terrain():
    """Active les boutons bout_charger et bout_sauv et désactive le bouton
    
    bout_terrain. Puis, elle génère le terrain du jeu à condition d'avoir
    recueillies les données de l'utilisateur.
    """
    global compteur_formulaire, racine, canvas
    bout_charger.config(state="normal")
    bout_sauv.config(state="normal")
    bout_terrain.config(state="disabled")
    compteur_formulaire += 1
    if liste([]):  
        for i in range(NB_COL):
            tableau.append([0]*NB_LIG)
        racine = tk.Tk()
        racine.title("Terrain de jeu")
        canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
        canvas.grid(column=0, row=0, columnspan=2)
        grille()
        nombre_etape()
        racine.bind("<1>", personnage)
        racine.bind("<Right>", droite)
        racine.bind("<Left>", gauche)
        racine.bind("<Up>", haut)
        racine.bind("<Down>", bas)
        racine.bind("<Return>", annuler) 
        racine.mainloop()


def grille():
    """La fonction crée la grille composé de carré marrons ou bleus avec

    les données fournies par l'utilisateur.
    """
    global i, j
    for i in range(NB_COL): 
        for j in range(NB_LIG):
            if pourcentage():     
                case(i, j, "eau")
            else: 
                case(i, j, "terre")           


def pourcentage():
    """La fonction attribue True ou False à chaque case, en fonction du
    
    pourcentage donné par l'utilisateur.
    """
    for nb in range(100):         
        nb = rd.randint(1,99)  
        if nb <= P:              
            return True
        else: 
            return False
    

def case(a, b, élément):     
    """Crée la case de coordonées a, b et lie la liste tableau avec le

    canvas en lui associant la couleur bleu sur le canvas et le chiffre 1
    dans la liste tableau si l'élément est l'eau. Sinon, lui associe 0
    et la couleur marron
    """
    x, y = a*COTE, b*COTE  
    if élément == "eau":
        tableau[a][b] = 1
        couleur = "blue"
    else:
        tableau[a][b] = 0
        couleur = "brown"
    canvas.create_rectangle((x, y), (x+COTE, y+COTE), fill=couleur)


def nb_case_eau(a, b):
    """Renvoie le nombre de cases bleus (recouverte d'eau) autour de la case
    
    de coordonnées (a, b).
    """
    compteur_eau = 0
    for y in range(max(0, a-K), min(NB_COL, (a+K)+1)):              
        for z in range(max(0, b-K), min(NB_LIG, (b+K)+1)):          
            if tableau_memoire[y][z] == 1 and [y, z] != [a, b]:  
                compteur_eau += 1
    return compteur_eau


def conversion(a, b):
    """Si le nombre de case d'eau est supérieur ou égale à la valeur du
    
    voisinnage en a, b appel la fonction case_eau(a, b, eau) sinon 
    case(a, b, terre).
    """
    if nb_case_eau(a, b) >= T:
        case(a, b, "eau")
    else:
        case(a, b, "terre")


def etape():
    """Copie le tableau initial dans la variable tableau_mémoire afin de
    
    faire une étape de conversion toutes les cases du canvas, sans etre
    influencé par les conversions précédentes.
    """
    global tableau_memoire
    tableau_memoire = cp.deepcopy(tableau)
    for i in range(NB_COL):
        for j in range(NB_LIG):
            conversion(i, j)
    tableau_memoire = tableau
    

def nombre_etape():
    """Réalise n fois la fonction étape si n>0, si n=0 réalise une copie

    du tableau dans la variable tableau_mémoire.
    """
    global tableau_memoire
    if N > 0:
        for i in range(N):
            etape()
    elif N == 0:
        tableau_memoire = cp.deepcopy(tableau)


def personnage(event):
    """Creer le personnage sur une case terre, là ou l'utilisateur à cliqué

    et appel sauvegarde_deplacement, sinon la fonction supprime le
    personnage.
    """
    global compteur_clic, perso, x0, y0, x1, y1
    global liste_sauvegarde, liste_touche
    a,b = event.x // COTE, event.y // COTE
    x, y = a*COTE, b*COTE
    if compteur_clic % 2 == 0:
        if tableau_memoire[a][b] == 0:
            compteur_clic += 1
            perso = canvas.create_rectangle((x, y),
                                            (x+COTE, y+COTE),
                                            fill="red")   
            x0, y0, x1, y1 = canvas.coords(perso)
            sauvegarde_deplacement()
    else:
        canvas.delete(perso)
        compteur_clic += 1
        liste_sauvegarde = []
        liste_touche = ["Début"]


def verifie_droite(abscisse0, abscisse1):   
    """Renvoie True si le maximum des abscisses est inférieur à la LARGEUR"""
    return max(abscisse0, abscisse1) < LARGEUR


def verifie_gauche(abscisse0, abscisse1):  
    """Renvoie True si le minimum des abscisses est supérieur à 0""" 
    return 0 < min(abscisse0, abscisse1)


def verifie_haut(ordonnee0, ordonnee1):   
    """Renvoie True si le minimum des ordonnees est supérieur à 0""" 
    return 0 < min(ordonnee0, ordonnee1)


def verifie_bas(ordonnee0, ordonnee1):   
    """Renvoie True si le maximum des ordonnees est inférieur à la HAUTEUR""" 
    return max(ordonnee0, ordonnee1) < HAUTEUR


def verifie_case(a, b):
    """Etudie l'état de la case de coordonnées a, b et renvoie True si la
    
    case étudié est de la terre (correspond à 0).
    """
    compteur_nb_eau = 0         
    if tableau_memoire[a][b] == 1:  
        compteur_nb_eau += 1
    if compteur_nb_eau == 0:
        return True


def presence_perso():
    """Renvoie vraie si le personnage existe"""
    if canvas.coords(perso) != []:
        return True


def droite(event):
    """Permet ou pas le déplacement du personnage vers la droite et appelle
    
    la fonction sauvegarde_deplacement puis derniere_touche.
    """
    global perso, x0, y0, x1, y1 
    i, j = int(x0//COTE), int(y0//COTE)
    if verifie_droite(x0, x1) and verifie_case(i+1, j) and presence_perso():
        canvas.move(perso, COTE, 0) 
        x0, y0, x1, y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        derniere_touche("Autre")


def gauche(event):
    """Permet ou pas le déplacement du personnage vers la gauche et appelle
    
    la fonction sauvegarde_deplacement puis derniere_touche.
    """
    global perso, x0, y0, x1, y1 
    i, j = int(x0//COTE), int(y0//COTE)
    if verifie_gauche(x0, x1) and verifie_case(i-1, j) and presence_perso():
        canvas.move(perso, -COTE, 0) 
        x0, y0, x1, y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        derniere_touche("Autre")

 
def haut(event):
    """Permet ou pas le déplacement du personnage vers le haut et appelle

    la fonction sauvegarde_deplacement puis derniere_touche.
    """
    global perso, x0, y0, x1, y1 
    i, j = int(x0//COTE), int(y0//COTE)
    if verifie_haut(y0, y1) and verifie_case(i, j-1) and presence_perso():
        canvas.move(perso, 0, -COTE) 
        x0, y0, x1, y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        derniere_touche("Autre")


def bas(event):
    """Permet ou pas le déplacement du personnage vers le bas et appelle

    la fonction sauvegarde_deplacement puis derniere_touche.
    """
    global perso, x0, y0, x1, y1 
    i, j = int(x0//COTE), int(y0//COTE)
    if verifie_bas(y0, y1) and verifie_case(i, j+1) and presence_perso():
        canvas.move(perso, 0, COTE) 
        x0, y0, x1, y1 = canvas.coords(perso)
        sauvegarde_deplacement()
        derniere_touche("Autre")


def sauvegarde_deplacement():
    """Ajoute dans la liste_sauvegarde les coordonnées successivement

    occupées par le personnage.
    """
    liste_sauvegarde.append(canvas.coords(perso))


def annuler(event):
    """Si la liste contient au moins 2 éléments, permet à l'utilisateur

    de revenir à l'avant dernière position, puis supprime ces coordonnées
    et appelle la fonction derniere_touche.
    """
    global x0, y0, x1, y1, perso, liste_sauvegarde, avant_derniere_position
    if len(liste_sauvegarde) >= 2 and presence_perso():
        x0, y0, x1, y1 = liste_sauvegarde[-2]
        avant_derniere_position = liste_sauvegarde[-2]
        canvas.coords(perso, x0, y0, x1, y1)
        del liste_sauvegarde[-2]
        derniere_touche("Retour")


def derniere_touche(x):
    """Ajoute dans une liste la dernière touche sur laquelle l'utilisateur

    a cliqué à condition que le dernier élément de la liste soit différent
    de cette touche et appel gestion_annuler."""
    if liste_touche[-1] != x:
        liste_touche.append(x)
        gestion_annuler()


def gestion_annuler():
    """Si l'utilisateur à cliqué sur retour puis sur une autre touche,
    
    l'avant dernière position est replacée dans la liste pour que le perso
    puisse revenir desssus.
    """
    if liste_touche[-2:] == ["Retour", "Autre"]:
        liste_sauvegarde[-2] = avant_derniere_position


def sauvegarder_terrain():
    """Sauvegarde le tableau_memoire dans le fichier sauvegarde_terrain.txt
    et appelle la fonction sauvegarde_perso en fonction de la présence ou
    pas du personnage."""
    fic = open("sauvegarde_terrain.txt", "w")
    for i in range(NB_COL):
        for j in range(NB_LIG):
            fic.write(str(tableau_memoire[i][j])+"\n")
    fic.close()
    if presence_perso():
        sauvegarder_perso(0)
    else:
        sauvegarder_perso(-1)
        

def sauvegarder_perso(x):
    """Sauvegarde les coordonnées du perso dans le fichier
    
    sauvegarde_perso.txt.
    """
    global perso
    if x == 0:
        fic = open("sauvegarde_perso.txt", "w")
        fic.write(str(canvas.coords(perso)[x])
                +" "+str(canvas.coords(perso)[x+1])
                +" "+str(canvas.coords(perso)[x+2])
                +" "+str(canvas.coords(perso)[x+3]))
        fic.close()
    else:
        fic = open("sauvegarde_perso.txt", "w")
        fic.write("")
        fic.close()


def charger_terrain():
    """Charge le fichier sauvegarde_terrain.txt pour dessiner la grille
    
    et appelle la fonction charger_perso.
    """
    fic = open("sauvegarde_terrain.txt", "r")
    compteur = 0
    for ligne in fic:
        i, j = compteur // NB_LIG, compteur % NB_LIG
        n = int(ligne)
        x, y = i * COTE, j * COTE
        if n == 0:
            canvas.create_rectangle((x, y),(x+COTE, y+COTE),fill="brown")
            tableau_memoire[i][j] = 0
        else:
            canvas.create_rectangle((x, y),(x+COTE, y+COTE),fill="blue")
            tableau_memoire[i][j] = 1
        compteur += 1
    fic.close()
    charger_perso()


def charger_perso():
    """Charge le fichier sauvegarde_perso.txt pour dessiner ou pas le
    personnage sur la grille."""
    fic = open("sauvegarde_perso.txt", "r")
    global perso, x0 , y0, x1, y1, liste_sauvegarde, liste_touche
    COTE = 20
    liste_sauvegarde = []
    liste_touche = ["Début"]
    for ligne in fic:
        if ligne != "":
            x0 = int(float(ligne.split()[0]))
            y0 = int(float(ligne.split()[1]))
            x1 = int(float(ligne.split()[2]))
            y1 = int(float(ligne.split()[3]))
            perso = canvas.create_rectangle((x0, y0),
                                            (x0+COTE, y0+COTE),
                                            fill="red")
            sauvegarde_deplacement()
    fic.close()


###############################################
#Programme principal

racine = tk.Tk()
racine.title("Programmation du terrain de jeu")
formulaire()
racine.mainloop()














