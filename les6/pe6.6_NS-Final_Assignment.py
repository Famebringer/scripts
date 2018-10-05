def standaardprijs(afstandKM):
    res = 0
    vastbedrag = 15
    if afstandKM <50:
        res = res + afstandKM*0.80
    else:
        res = res + 15 + afstandKM*0.60
    return res


def ritprijs(leeftijd, weekendrit, afstandKM):

    if weekendrit == " Ja " and (leeftijd >=65 or leeftijd <=12):
        return standaardprijs(afstandKM) *0.65

    elif weekendrit == " Ja " and (leeftijd <65 or leeftijd >12):
        return standaardprijs(afstandKM) *0.60
    elif weekendrit == " Nee " and (leeftijd >=65 or leeftijd <=12):
        return standaardprijs(afstandKM) * 0.7
    else:
        return standaardprijs(afstandKM)


rp= ritprijs(22, " Nee ", 40)
print (rp)



