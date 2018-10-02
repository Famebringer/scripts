def standaardprijs(afstandKM):
    res = 0
    vastbedrag = 15
    for i in afstandKM:
        if i <50:
            res = res + i*0.80

        else:
            print (15 + 0.60 * 15)
    return res

# print(standaardprijs([50]))

def ritprijs(leeftijd, weekendrit, afstandKM):
    res = 35
    jo_oud = 30
    for a in weekendrit:
        if a == " Ja ":
            res = res / standaardprijs(afstandKM)
            return res



     for a in leeftijd
          elif b <=12 and  >65:
            jo_oud = jo_oud / standaardprijs(afstandKM)
            return res

rp= ritprijs(22, " Ja ", 60)



