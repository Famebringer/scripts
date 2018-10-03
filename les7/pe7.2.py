def convert(celsius):
    res = 0
    res = res + celsius * 1.8 + 32
    return res


def table():
    for celsius in range( -30 , 40, 10):
        print (convert(celsius))
        print(celsius)
    return table

table()

