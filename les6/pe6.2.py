# Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst. Ga ervan uit dat dit een list is met integers.
#  De return-waarde van de functie moet de som (optelling) van de getallen in de lijst zijn!
 #  Tip: bekijk nog eens de list-functies (Perkovic, blz. 28).

def listsum(list):
    ret=0
    for i in list:
        ret+=i
    return ret
