# Exemple code basique
from tkinter import *
from tkinter import ttk
root = Tk() # Créer une instance Tk classe qui initialise et créer les ressources associées à l'interpreteur Tcl, créer aussi une fenêtre en haut
frm = ttk.Frame(root, padding=10) # Créer une fenêtre widget qui contiendra un label et un bouton 
frm.grid() # Utilisé pour pour spécifier la position du label qui contiendra le widget
ttk.Label(frm, text="Hello World!").grid(column=0, row=0) # Créer un label widget tenant un espace texte statique
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0) # Créer un bouton widget, le place à droite du label quand il est pressé il détruit la fenêtre principale
root.mainloop() # Met tout en place graphiquement et l'affiche sur l'écran tout en prenant les commandes utilisateur jusqu'à ce que le programme soit fermé