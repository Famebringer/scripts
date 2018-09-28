#Schrijf (en test) de functie kwadraten_som() die 1 parameter heeft: grondgetallen.
# Dit is een list is met integers.
# De return-waarde van de functie is de som van de kwadraten van alle positieve getallen in de lijst!
# Een lijst van [ 4, 5, 3, -81 ] heeft als return-waarde dus 50 (namelijk 16 + 9 + 25).

def kwadraten_som(grondgetallen):
    res = 0
    for i in grondgetallen:
        if i >0:
            res = res + i**2
    return res


#return sum([ i**2 for i in grondgetallen]      ANDERE MANIER VAN BOVENSTAANDE

print(kwadraten_som([5,7,8, -2]))


#return sum([ i**2 for i in grondgetallen]      ANDERE MANIER VAN BOVENSTAANDE
