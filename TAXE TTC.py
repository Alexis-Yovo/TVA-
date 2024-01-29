##### Calculer le TTC à partir de HT et de la TVA
HT=(float(input("Le prix HT : ")))
TVA = (float(input("Le TVA: ")))
TTC= HT*(1+TVA/100)
TTC = round(TTC,2) # ne prendre que jusqu'a centimes
print("Le prix TTC : ",TTC)
