infile = open('kaartnummer.txt', 'r')
data = infile.readlines() #bestand
kaartnummers = []


for regel in data:
    kaartnummers.append(int(regel.split(":")[1]))


print('het grootste getal is: ' + (max(kaartnummers) +