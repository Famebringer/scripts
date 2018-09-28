# Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst. Ga ervan uit dat dit een list is met integers.
#  De return-waarde van de functie moet de som (optelling) van de getallen in de lijst zijn!
 #  Tip: bekijk nog eens de list-functies (Perkovic, blz. 28).


def som(getallenlijst):
    res = max (getallenlijst) - min (getallenlijst)
    return res

print(som([7,9,8,2]))


def som(getallenlijst2):
    res = sum(getallenlijst2)
    return res
print(som([1,2,3,4]))