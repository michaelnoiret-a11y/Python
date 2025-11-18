def calcule(num1, operator, num2):
    num1=int(input("Saisir un nombre entier: "))
    operator=str(input("Saisir un opérateur: "))
    num2=int(input("Saisir un nombre entier: "))
    resultat = {num1} + {operator} + {num2}
    return resultat

print(calcule(num1="", operator="", num2="" ))