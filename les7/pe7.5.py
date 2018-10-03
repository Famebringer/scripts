import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y %H:%M:%S")

appendFile = open ('hardlopers.txt', 'a')
appendFile.write ( s + " Piet ")
appendFile.write("\n")
appendFile.close()
