# klein programma
def lengte(lang_genoeg):
    lengte = eval(input(' Wat is jouw lengte in centimeters?: '))
    if lengte >= 120:
        print (" Je bent lang genoeg voor de attractie")
    else:
        print (" Sorry je bent te klein!")

lengte(90)