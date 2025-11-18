def pair_impair(nombre):
    #nombre=int(input("Saisir un nombre entier: "))
    if nombre > 0:
        print(f"{nombre} est positif")
    elif nombre < 0:
        print(f"{nombre} est négatif")
    else:
        print(f"{nombre}")    

pair_impair(nombre=3)
pair_impair(nombre=-1)
pair_impair(nombre=0)
pair_impair(nombre=3.14)
