"""import json

donnees = {
    "nom": "Stéphane ROBERT",
    "age": 29,
    "adresse": {
        "rue": "456 avenue des Champs",
        "ville": "Lyon",
        "code_postal": "69001"
    }
}

# Écriture des données dans un fichier JSON avec encodage UTF-8
with open('donnees_utilisateur.json', 'w', encoding='utf-8') as fichier:
    json.dump(donnees, fichier, indent=4, ensure_ascii=False)
    donnees["site"] = input("Saisir le nom du site")
    donnees["password_hash"].append(password_hash)
    if donnees["site"] and donnees["password_hash"] == donnees["site"] and donnees["password_hash"]:
        print("Déjà enregistré")
        print(donnees["password_hash"])"""
"""
import random

majusculealphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculealphabets = "abcdefghijklmnopqrstuvwxyz"
caracteres_speciaux = "!@#$%^&*#"
alphanumeriques = "0123456789"
password = random.choices(majusculealphabets,minusculealphabets, caracteres_speciaux, alphanumeriques)
print(password)

while password :
    if len(password) <= 8 and majusculealphabets not in password and caracteres_speciaux not in password and alphanumeriques not in password and minusculealphabets not in password:
            print("Mot de passe ne convient pas aux exigences de sécurité à respecter, réessayer ")

    else:
        print("Mot de passe accepté")
        break"""