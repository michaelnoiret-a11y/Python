"""#import random
#import hashlib

majusculealphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculealphabets = "abcdefghijklmnopqrstuvwxyz"
caracteres_speciaux = "!@#$%^&*#"
alphanumeriques = "0123456789"
password = str(input("Saisir un mot de pass correspondant aux exigences de sécurité: "))
for i in password:
    if len(password) >= 8 and majusculealphabets in password == True and minusculealphabets in password ==  True and caracteres_speciaux in password == True and alphanumeriques in password == True:

        print("Mot de passe accepté")
    
    else:
        print("Mot de passe ne convient pas aux exigences de sécurité à respecter, réessayer ")

#Chat GPT exemple:
caracteres_speciaux = "!@#$%^&*#"


def mot_de_passe_valide(password):
    return (
        len(password) >= 8
        and any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in caracteres_speciaux for c in password)
    )

password = input("Saisir un mot de passe : ")

while not mot_de_passe_valide(password):
    print("\n❌ Mot de passe invalide. Il doit contenir :")
    print(" - au moins 8 caractères")
    print(" - au moins 1 minuscule")
    print(" - au moins 1 majuscule")
    print(" - au moins 1 chiffre")
    print(" - au moins 1 caractère spécial parmi :", caracteres_speciaux)
    password = input("\nRéessayez : ")

print("\n✅ Mot de passe accepté !")

Exemple 2:"""
caracteres_speciaux = "!@#$%^&*#"

password = input("Saisir un mot de passe correspondant aux exigences de sécurité : ")

# Flags
contient_min = False
contient_maj = False
contient_chiffre = False
contient_special = False

# Parcours du mot de passe
for c in password:
    if c.islower():
        contient_min = True
    if c.isupper():
        contient_maj = True
    if c.isdigit():
        contient_chiffre = True
    
    # Vérification sans utiliser "in"
    for special in caracteres_speciaux:
        if c == special:
            contient_special = True

# Vérification finale
if len(password) >= 8 and contient_min and contient_maj and contient_chiffre and contient_special:
    print("Mot de passe accepté")
else:
    print("Mot de passe ne convient pas aux exigences de sécurité.")
"""
caracteres_speciaux = "!@#$%^&*#"

def mot_de_passe_valide(password):
    # Vérifications des conditions
    longueur_ok = len(password) >= 8
    min_ok = any(c.islower() for c in password)
    maj_ok = any(c.isupper() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_ok = any(c in caracteres_speciaux for c in password)

    return longueur_ok and min_ok and maj_ok and digit_ok and special_ok

# Boucle jusqu'à ce que le mot de passe soit valide
while True:
    password = input("Saisir un mot de passe correspondant aux exigences de sécurité : ")
    
    if mot_de_passe_valide(password):
        print("\n✅ Mot de passe accepté !")
        break
    else:
        print("\n❌ Mot de passe invalide. Il doit contenir :")
        print(" - au moins 8 caractères")
        print(" - au moins 1 minuscule")
        print(" - au moins 1 majuscule")
        print(" - au moins 1 chiffre")
        print(" - au moins 1 caractère spécial parmi :", caracteres_speciaux)
        print("Réessayez.\n")
    
"""