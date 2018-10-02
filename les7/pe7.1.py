month = input(" Voer de maandnummer in")
def seizoen(maand):
    if maand in [1, 2, 3]:
        seizoen = ' Winter '
    elif maand in [ 4, 5, 6]:
        seizoen = ' Lente '
    elif maand in [ 7, 8, 9]:
        seizoen = ' Zomer '
    else:
        seizoen = ' Herft'
    return seizoen

print(seizoen(eval(month)))