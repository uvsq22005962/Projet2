# Projet2 Génération terrain de jeu

Les membres ayant participé à l'écriture du code sont:
# Cyril CLOVIS
# Dylan THUILLIER
# Ahmadou bamba SOUM
# Olivier GABRIEL

Claude Chibout et Abdelkarim Bouraoui n'ont pas du tout participé au projet.


# Explication du code:

Premièrement, nous avons réussi tous les étapes qui composent le projet donc il ne devrait pas y avoir d'erreur.  

# Formulaire

Lorsque vous lancerez le projet, une interface apparaitra. C'est un formulaire qui doit IMPERATIVEMENT etre rempli selon l'ordre suivant: 
De gauche à droite et de haut en bas.

Exemple:
Vous souhaitez avoir 35 colonnes, vous rentrez 35 puis VALIDEZ VOTRE VALEUR en cliquant sur Valider, seulement après l'avoir validée, vous pourrez passer au nombre de lignes. Cette fois-ci, vous souhaitez garder la valeur par défaut pour le nombre de lignes. Donc, vous voulez 50 lignes, cliquez sur Défaut (les valeurs par défaut sont indiqués sur l'interface). Puis, vous pourrez passer à la probabilité de case recouverte d'eau et ainsi de suite jusqu'à l'ordre. Ce qu'il faut retenir, c'est que vous pourrez passer au paramètre suivant à condition d'avoir rentré et validé une valeur ou d'avoir cliqué sur défaut.
Vous pourrez ensuite générer le terrain à condition d'avoir rentré toutes les valeurs demandées.
ATTENTION à ne pas confondre les boutons Valider et Défaut. 

# Terrain de jeu

Le personnage est assimilé à un carreau rouge. Vous pouvez le créer en cliquant (clique gauche) sur une case terre (marron). Vous pouvez le supprimer en cliquant une seconde fois sur le clique gauche et ce n'importe où sur le canvas. SI le personnage existe, vous pouvez le déplacer grace aux touches directionnelles du clavier. Vous pouvez également revenir sur l'avant dernière position occupée en cliquant sur la touche Entrée. Si vous créez un personnage, puis le supprimez, puis en créez un nouveau, si vous n'avez pas bougé entre temps, vous ne pourrez pas revenir en arrière. 

# Sauvegarder et Charger

Vous ne pouvez pas sauvegarder et/ou charger si vous avez fermer la fenetre "Terrain de jeu". Par ailleurs, si vous sauvegarder le terrain de jeu (en y incluant un éventuel personnage), vous pouvez le chargez directement après (ce n'est pas très utile, mais c'est bon à savoir). CEPENDANT, si vous avez sauvegardé le Terrain puis fermé le programme, la condition pour pouvoir le charger lorsque que vous relancerez le programme est la suivante:
Vous devez impérativement utiliser le meme nombre de colonnes et de lignes que pour la session précédente (on vous conseille donc de garder les valeurs par défauts pour le nombre de colonnes et de lignes si vous voulez tester la fonction sauvegarder/charger).
Nous précisons également que le programme fait intervenir 2 fenetres. Ainsi, si vous voulez bouger un personnage que vous avez fait revenir grace au chargement, cliqué sur la barre blanche contenant "Terrain de jeu".

Exemple:
Si vous avez rentré 35 colonnes et 46 lignes pour la session n-1. Pour charger la session n-1 lors de la session n, vous devez rentrer 35 colonnes et 46 lignes. (Vous pouvez évidemment changer le reste des paramètres).

# Etude du code 

Cette partie est consacrée à la partie du sujet suivante:
"Vous étudierez la manière dont les paramètres influent sur la probabilité que le personnage puisse joindre le haut et le bas de la grille en se déplaçant."

Nous rappelons que les paramètres sont p, n, t, k.

Par définition, p représente la probabilité de case recouverte d'eau. Autrement dit, si p augmente, la probabilité que le personnage puisse joindre le haut et le bas de la grille en se déplaçant diminue puisqu'il ne peut pas circuler sur les cases d'eau.

n répresente le nombre d'étape
T représente le nombre minimun de case d'eau autour d'une case pour qu'elle se transforme en eau
k réprésente l'ordre

Supposons (n, p) > 0 et T est grand (T >= 9 à l'ordre 1), qu'importe le nombre d'étape, tout le terrain sera recouvert de terre (en effet il ne peut jamais y avoir plus de 8 cases recouverte d'eau dans le voisinnage à l'ordre 1). Autrement dit, si T augmente, la probabilité que le personnage puisse joindre le haut et le bas de la grille en se déplaçant augmente.

Supposons maintenant (T = 9) et (k >= 2), cette fois ci le terrain ne sera pas exclusivement recouvert de terre, or à l'ordre 1 tout aurait été recouvert de terre, autrement dit, si k augmente, la probabilité que le personnage puisse joindre le haut et le bas de la grille en se déplaçant diminue.

Le nombre d'étape n'a aucun effet directe sur la probabilité que le personnage puisse joindre le haut et le bas de la grille. En effet, n fait intervenir n fois les paramètres T et k pour chacune des cases de la grille. Son influence sur la probabilité de joindre les 2 bouts est donc indirecte puisqu'elle dépend des paramètres T et k. 

# Précision sur le code

Dans la fonction formulaire (1 ere fonction du code), la fonction recueille_donnee prend en paramètre des nombres entiers. L'avantage était ici de pouvoir "numéroter" les boutons, entrées et labels mais aussi de prendre en paramètre des éléments qui "existent" déjà sans qu'on ai eu à les définir.