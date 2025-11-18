def fruits_legumes(type, saison):
    type=input("Saisir un type; fruits ou légumes: ")
    saison=input("Saisir une saison: ")
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print("Artichaut, aubergine, navet")

fruits_legumes(type="", saison="")       