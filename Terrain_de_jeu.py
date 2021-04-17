#########################################
# groupe  2 MPCI 6
# Cyril CLOVIS
# Dylan THUILLIER
# Abdel karim BOURAOUI
# Ahmadou bamba SOUM
# Olivier GABRIEL
# https://github.com/uvsq22005256/projet_incendie
# https://discord.gg/fNQpuPM3yQ
#########################################
#Import des fonctions
import tkinter as tk
import random as rd

###############################################
#Variables
color_canv = "grey30"
couleur_quadr = 'grey60'
cote = 20
largeur_canv = int(input('Choisir le nombre de colonnes:'))
hauteur_canv = int(input('Choisir le nombre de lignes:'))
p = int(input('Choisi la probabilité de case bleu en %'))
T = int(input("Choisir le nombre minimum de cases voisines pour appliquer la règle:"))
n=int(input('Combien d_activation pour l_automate:'))
nb_col = (largeur_canv*20) // cote
nb_lig = (hauteur_canv*20) // cote
perso = 0
m = 1



###############################################
#Fonctions 


def go():
    """Effectue la fonction comptage et l'arrête au bout de n défini par l'utilisateur""" 
    global n
    x = 0
    while x != n:
            comptage()
            x += 1





def liste() :
    """Créer une liste a deux dimensions"""
    l = list(range(nb_lig))
    for i in l : 
        l[i] = list(range(nb_lig))
        for j in range(nb_col) : 
            l[i][j] = 0
    return l



def regle():
    """Applique la règle du nombre de voisin autour de la case d'eau pour définir sa couleur"""
    global T 
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 1 and c[i][j] >= T :
                 ini(i, j)
            elif l[i][j] == 0 and c[i][j] >= T :
                 ini(i,j)
            elif l[i][j] == 1 and c[i][j] < T :
                 détruit(i, j)
            elif (l[i][j] == 0 and c[i][j] < T) :
                 détruit(i, j)




def comptage() :
    """Compte le nombre de case voisine autour d'une case d'eau et applique la règle """ 
    global m
    #k =int(input('Choisis la distance des cases voisines:'))
    cpt = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0 and j == 0 : #Case tout en haut a gauche
                cpt = l[0][1] + l[1][0] + l[1][1]
                c[0][0] = cpt
            elif i == 0 and j == nb_col-1:#Case tout en haut a droite
                cpt = l[0][nb_col-2] + l[1][nb_col-2] + l[1][nb_col-1]
                c[0][nb_col-1] = cpt
            elif i == nb_lig-1 and j == 0 :#Case tout en bas a gauche
                cpt = l[nb_lig-2][0] + l[nb_lig-2][1] + l[nb_lig-1][1]
                c[nb_lig-1][0] = cpt
            elif i == 0 and j == nb_col-1 :#Case tout en bas a droite
                cpt = l[0][nb_col-2] + l[1][nb_col-1] + l[1][nb_col-2]
                c[0][nb_col-1] = cpt                
            elif 0 < i < nb_lig-1 and j == 0 :#Bord de gauche
                cpt = l[i-1][0] + l[i-1][1] + l[i][1] + l[i + 1][1] + l[i+1][0]
                c[i][0] = cpt
            elif 0 < i < nb_lig-1 and j == nb_col-1 :#Bord de droite
                cpt = l[i-1][nb_col-1] + l[i-1][nb_col-2] + l[i][nb_col-2] + l[i+1][nb_col-1] + l[i+1][nb_col-2]
                c[i][nb_col-1] = cpt
            elif i == 0 and 0 < j < nb_col-1 :#Bord du haut
                cpt = l[0][j-1] + l[1][j-1] + l[1][j] + l[1][j+1] + l[0][j+1]
                c[0][j] = cpt
            elif i == nb_lig-1 and 0 < j < nb_col-1 : #Bord du bas 
                cpt = l[nb_lig-1][j-1] + l[nb_lig-2][j-1] + l[nb_lig-2][j] + l[nb_lig-2][j+1] + l[nb_lig-1][j+1]
                c[nb_lig-1][j] = cpt
            elif 1 <= i <= nb_lig-2 and 1 <= j <= nb_col-2 :#Tout le reste 
                cpt = l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1] + l[i+1][j] + l[i+1][j-1] + l[i][j-1]
                c[i][j] = cpt
    regle()           
    
 





def case_eau() :
    """Créer des cases bleu avec une probabilitée définie par l'utilisateur"""
    global p 
    for j in range(nb_lig) :
        for i in range(nb_col) :
            nb = rd.randint(0,100)
            if nb <= p :
                ini(i, j)



     

  

def ini(x, y):
    """Vérifie l'état de la case dans la liste l et si elle vaut 1 change la case en bleu """
    l[x][y] = 1
    canvas.delete(r[x][y])
    r[x][y] = canvas.create_rectangle(x * cote, y * cote, cote + x * cote, cote + y *cote,width = 0.1, fill = 'blue', outline ='white')
    

def détruit(x, y) :
    """Vérifie l'état de la case dans la liste l et si elle vaut 0 change la case en gris """
    l[x][y] = 0
    canvas.delete(r[x][y])
    r[x][y] = canvas.create_rectangle(x * cote, y * cote, cote + x * cote, cote + y *cote, width= 0.1 ,fill = 'grey', outline = 'white')



def crée_personnage(event) :
    """Créer un personnage sur le terre"""
    global perso
    global l
    global m
    x = event.x
    y = event.y
    rectangle_proche = canvas.find_closest(x , y)
    x1 , y1 , x2 , y2 = canvas.coords(rectangle_proche)
    if m == 1 and l[x//20][y//20] == 0 :
        m += 1
        perso = canvas.create_rectangle(x1,y1,x2,y2,width = 0.1, fill = 'red', outline = 'white')
    elif m == 2 :
        m -= 1
        canvas.delete(perso)







def mouvement_droite(event) :
    """déplace le personnage à droite"""
    global perso, l
    x1 , y1 , x2 , y2 = canvas.coords(perso)
    x3 , y3 = int(x2//20) , int((y2-10)//20)
    if x2 + 20 > largeur_canv * 20 or l[x3][y3] == 1 :
        pass
    else :
        canvas.move(perso, cote, 0)




def mouvement_gauche(event) :
    """déplace le personnage a gauche""" 
    global perso, l
    x1 , y1 , x2 , y2 = canvas.coords(perso)
    x3 , y3 = int((x1-20)//20) , int((y1+10)//20)
    if x1 - 20 < 0 or l[x3][y3] == 1:
        pass
    else :
        canvas.move(perso, -cote , 0)





def mouvement_haut(event) :
    """déplace le personnage vers le haut """ 
    global perso, l
    x1 , y1 , x2 , y2 = canvas.coords(perso)
    x3 , y3 = int((x1+10)//20) , int((y1 -20)//20)
    if y1 - 20 < 0 or l[x3][y3] == 1:
        pass
    else :
        canvas.move(perso,0, -cote)





def mouvement_bas(event):
    """déplace le personnage vers le bas"""
    global perso
    x1 , y1 , x2 , y2 = canvas.coords(perso)
    x3 , y3 = int((x1+10)//20) , int(y2//20)
    if y2 + 20 > hauteur_canv * 20 or l[x3][y3] == 1:
        pass
    else :
        canvas.move(perso, 0 , cote)


    


###############################################
#Programme principal
r = liste() #Référence toute les positions des rectangles dans une liste
c = liste() #Liste qui permet de compter le nombre de voisin
l = liste() #Liste qui permet de connaître l'état d'une case du quadrillage


racine = tk.Tk()
racine.title("Terrain_de_jeu")
canvas = tk.Canvas(racine, bg = color_canv, width = (largeur_canv*20), height =(hauteur_canv*20))
for i in range(nb_lig):
        for j in range(nb_col):
            r[i][j] = canvas.create_rectangle(i * cote , j * cote, cote + i * cote, cote + j * cote,width = 0.1, fill = 'grey', outline = 'white')
bouton_génération =tk.Button(racine, text = 'génération_map')
bouton_sauv = tk.Button(racine,text = 'sauvegarder')
bouton_charg = tk.Button(racine,text = 'charger')
bouton_para = tk.Button(racine,text = 'paramètre')
bouton_génération.grid(column = 0,row = 1)
bouton_sauv.grid(column = 0,row = 2)
bouton_charg.grid(column = 0, row = 3)
bouton_para.grid(column = 1, row = 3)
canvas.bind("<Button-1>", crée_personnage)
racine.bind("d",mouvement_droite)
racine.bind("z",mouvement_haut)
racine.bind("s",mouvement_bas)
racine.bind("q",mouvement_gauche)      
canvas.grid(column = 1, row = 2)
case_eau()
go()
racine.mainloop()