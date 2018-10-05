new_list = []
zin = eval(input("Geef lijst met minimaal 10 strings: "))

for strings in zin:
    if len(strings) == 4:
        new_list.append(strings)
1
print(" De nieuw-gemaakte lijst met alle vier-letter strings is:", str(new_list))