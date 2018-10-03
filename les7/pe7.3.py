text = 'Jan Jansen heeft kaartnummer: 325255\nErik Materus heeft kaartnummer: 334343\n''Ali Ahson heeft kaartnummer: 235434\nEva Versteeg heeft kaartnummer: 645345\n''Jan de Wilde heeft kaartnummer: 534545\nHenk de Vrie heeft kaartnummer: 345355'

saveFile = open('kaartnummer.txt', 'w')

saveFile.write(text)
saveFile.close()

