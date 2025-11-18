def moyenne(note1,note2,note3):
    note1=int(input("Saisir valeur note: "))
    note2=int(input("Saisir valeur note: "))
    note3=int(input("Saisir valeur note: "))
    moyenne_etudiant = note1 + note2 + note3 / 3
    if moyenne_etudiant >= 15:
        print("Très bon élève")
    elif moyenne_etudiant >= 11:
        print("Bon élève")
    elif moyenne_etudiant >= 8:
        print("Eleve moyen")
    else:
        print("Eleve devant faire des efforts")

moyenne(note1="", note2="", note3="")                 