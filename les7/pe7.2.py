def convert(celsius):
    res = 0
    res = res + celsius * 1.8 + 32
    return res


def table():
    print('{:>3} {:>5}'.format ('F', 'C'))
    for celsius in range( -30 , 50, 10):
        print('{} {:5}'.format(convert(celsius), celsius))


table()

