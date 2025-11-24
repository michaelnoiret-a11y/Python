# Trouver syntaxe JSON pour ne pas écraser les données mais les joindre à la suite , choisir liste ou dictionnaire pour le recueil des mots de passe hachés
#import os
import random
import hashlib

majusculealphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculealphabets = "abcdefghijklmnopqrstuvwxyz"
caracteres_speciaux = "!@#$%^&*#"
alphanumeriques = "0123456789"
password = str(input("Saisir un mot de passe correspondant aux exigences de sécurité: "))

while password :
    if len(password) <= 8 and majusculealphabets not in password and caracteres_speciaux not in password and alphanumeriques not in password and minusculealphabets not in password:
            print("Mot de passe ne convient pas aux exigences de sécurité à respecter, réessayer ")
            password = str(input("Saisir un mot de pass correspondant aux exigences de sécurité: "))
            print("Voulez-vous que je génère le mot de passe ? ")
            if input() == "Y" or "y":
                password = random.choices(majusculealphabets,minusculealphabets, caracteres_speciaux, alphanumeriques)
            print(password)
            if input() == "N" or "n":
                print("Saisir un mot de passe correspondant aux exigences de sécurité: ")
                password = str(input("Saisir un mot de passe correspondant aux exigences de sécurité: "))
    else:
        print("Mot de passe accepté")
        sha256 = hashlib.sha256(password.encode())
        password_hash = sha256.hexdigest()
        print(f"Hash:{password_hash}")
        break


# import hashlib
# pwd = 'GeekPassword'
# s = '5gz'

# # Combine password and salt
# pwd_salt = pwd + s
# hashed = hashlib.sha256(pwd_salt.encode())
# print(hashed.hexdigest())


"""
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

Exemple 2:
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
Exemple 3:
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
