# klein programma

def lang_genoeg(lengte):
    if lengte >= 120:
        print (" Je bent lang genoeg voor de attractie")
    else:
        print (" Sorry je bent te klein!")


lengte = eval(input(' Wat is jouw lengte in centimeters?: '))
lang_genoeg(lengte)