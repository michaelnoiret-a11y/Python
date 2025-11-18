nom="PC"
prix_unitaire=900
quantite_en_stock=1
print(f"nom du produit :",nom,"prix_unitaire du produit:",prix_unitaire,"€","quantité en stock produit:",quantite_en_stock)
quantite_ajoutee=int(input("Ajouter quantité reçu du produit"))
nouveau_stock=quantite_en_stock + quantite_ajoutee
print(nouveau_stock)
prix_inflatation = prix_unitaire * 1.10
print(f"nom du produit :",nom,"prix_unitaire du produit:",prix_inflatation,"€","quantité en stock produit:",nouveau_stock)