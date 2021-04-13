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


###############################################
#Variables
largeur_canv = 500
hauteur_canv = 500
color_canv = "grey30"
nombre_de_ligne = input(int())
nombre_de_colonne = input(int())
couleur_quadr = 'grey60'
cote = 20
racine = tk.Tk()
canvas = tk.Canvas(racine, bg = color_canv, width = largeur_canv, height =hauteur_canv)



###############################################
#Fonctions
def quadrillage() :

    

###############################################
#Programme principal


racine.title("Terrain_de_jeu")
canvas.grid()
quadrillage()
racine.mainloop()