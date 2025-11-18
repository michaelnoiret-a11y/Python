def nombre_entier_positif(nombre):
    nombre = int(input("Saisir un nombre: "))
    if nombre % 2 == 0 and nombre != float and nombre > 0:
        print("Le nombre est bien un entier positif et pair ")
    elif nombre % 2 != 0 and nombre != int and nombre < 0:
        print("Le nombre est un décimale, négatif et impaire ")
    else:
        print("Ce n'est pas un nombre correspondant à la demande ")  

nombre_entier_positif(nombre=3)
nombre_entier_positif(nombre=-3)
nombre_entier_positif(nombre=3.14)
