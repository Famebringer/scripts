# het halen van een even reeks met een for loop

gelijke_nummers= []
oneven_nummers= []

for nummer in range(0,53):
	if nummer % 2 == 0:
		gelijke_nummers.append(nummer)
	else:
		oneven_nummers.append(nummer)

print(oneven_nummers)