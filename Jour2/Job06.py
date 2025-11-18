N=int(input("Saisir un entier supérieur à zéro (N): "))
i = 1
while i in range(1,11):
    if N > 0 and i < 6:
        print(f"{N} x {i} =",i*N)
        i+=1