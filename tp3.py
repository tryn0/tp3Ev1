from sys import argv

leer = open(argv[1],"r")
linea = leer.readline()
while linea:
  print(linea,end="")
  linea = leer.readline()
leer.close()

