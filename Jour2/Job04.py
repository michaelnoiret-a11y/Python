N=int(input("Saisir un entier supérieur à zéro (N): "))
for i in range(1,11):
    if N > 0:
        print(f"Table de multiplication de {i}")
        print(f"{N} x {i} =",i*N)
        i+=1
    