infile = open('kaartnummer.txt', 'r')
data = infile.read()
Characters = len(data)
Words = len(data.split())

Lines = len(data.splitlines())
print ("Deze file telt ",Lines, "regels")