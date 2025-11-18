def dessin_rectangle(width, height):
    width = int(input("Saisir la longueur: "))
    height = int(input("Saisir la hauteur :" ))
    print("|" + "-" * (width - 2) + "|")
    print("|" + " " * (width - 2) + "|")

dessin_rectangle(width="", height="")   