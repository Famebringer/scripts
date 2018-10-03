# Het maken van de file
text = 'Sample Text to Save\nNew Line!'

saveFile = open('exampleFile.txt', 'w')

saveFile.write(text)
saveFile.close()



# het appenden van de bovenstaande file
appendMe = '\nNew bit of information'

appendFile = open ('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close()

#het lezen van de file

readMe = open('exampleFile.txt', 'r').read()
print(readMe)

# appenden + enter naar volgende regel

appendFile = open ('hardlopers.txt', 'a')
appendFile.write ( s + " Piet ")
appendFile.write("\n")
appendFile.close()