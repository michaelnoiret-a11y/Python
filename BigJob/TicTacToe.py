# Exemple code basique
from tkinter import *
from tkinter import ttk

root = Tk() # Créer une instance Tk classe qui initialise et créer les ressources associées à l'interpreteur Tcl, créer aussi une fenêtre en haut
frm = ttk.Frame(root, padding=10) # Créer une fenêtre widget qui contiendra un label et un bouton 
frm.grid() # Utilisé pour pour spécifier la position du label qui contiendra le widget
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0) # Créer un label widget tenant un espace texte statique   
ttk.Button(frm, text="1 joueur", command=clicked).grid(column=0, row=0)
ttk.Button(frm, text="2 joueurs", command=clicked).grid(column=4, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=4) # Créer un bouton widget, le place à droite du label quand il est pressé il détruit la fenêtre principale
root.mainloop() # Met tout en place graphiquement et l'affiche sur l'écran tout en prenant les commandes utilisateur jusqu'à ce que le programme soit fermé

#if ttk.Button("Joueur 1" or "Joueur 2") is pressed:
top = Toplevel()
top.title("Tic Tac Toe")
top.mainloop()
board =[0:9]
signe = "X","O"
signe_in_board = str(input("Choisir un index où placer signe:"))
full = "X", "O"
player1 = str(input("Saisir pseudo de Player 1:"))
player2 = str(input("Saisir un pseudo pour Player 2"))
IA = "Zero"
if signe == "X" in board and player1 and not full:
    print("X" in board[""])
elif signe == "O" in board and player2 or IA and not full:
    print("O" in board[""])
else:
    print("Already full, try another place")
    
    if signe == "X"  in board[1,2,3/3,2,1 or 3,5,7/7,5,3 or 1,5,7/7,5,1 or 7,8,9/9,8,7] and player1:
        print("player1 win")
        break
    elif signe == "O" in board[1,2,3/3,2,1 or 3,5,7/7,5,3 or 1,5,7/7,5,1 or 7,8,9/9,8,7] and player2:
        print("player2 win")
        break
    elif signe == "O" in board[1,2,3/3,2,1 or 3,5,7/7,5,3 or 1,5,7/7,5,1 or 7,8,9/9,8,7 or ] and IA:
        print("IA win")
        break
    else:
        print("Withdrawl")
        break