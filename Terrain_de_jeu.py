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
largeur_canv = 1000
hauteur_canv = 1000
color_canv = "grey30"
couleur_quadr = 'grey60'
cote = 10
racine = tk.Tk()
canvas = tk.Canvas(racine, bg = color_canv, width = largeur_canv, height =hauteur_canv)



###############################################
#Fonctions
def case_eau() :
 nb = rd.randint(0,1)
 for j in range(101) :
    for i in range(101) :
            nb = rd.randint(0,1)
            if nb == 0 :
                canvas.create_rectangle((i * 10,j * 10),(10 + i * 10,10 + j* 10 ), fill='blue')
            else : 
                canvas.create_rectangle((i *10 ,j * 10), (10 + i * 10 , 10 + j * 10), fill = 'grey')



def quadrillage() :
 y = 0
 global hauteur_canv
 global largeur_canv

 while y <= hauteur_canv :
    canvas.create_line((0,y), (largeur_canv,y), fill=couleur_quadr)
    y += cote
 x = 0    
 while x <= largeur_canv :
    canvas.create_line((x,0), (x, hauteur_canv), fill=couleur_quadr)
    x += cote
    

###############################################
#Programme principal


racine.title("Terrain_de_jeu")
canvas.grid()
quadrillage()
case_eau()
racine.mainloop()