#Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt
# heeft en dat daarna het salaris uitprint


#Wat verdien je per uur: 3.80
#Hoeveel uur heb je gewerkt: 20
#20 uur werken levert 76.0 Euro op


geld = eval(input (' Wat verdien je per uur?: '))
tijd = eval(input (' Hoeveel uur heb je gewerkt?: '))
line1 = str(tijd) + ' uur werken levert ' + str(geld * tijd) + ' Euro op'

print(line1)