from sys import argv


leer = open(argv[1],'r')
lista = list()
linea = leer.readline()
while linea:
  lista.append(linea)
  linea = leer.readline()
leer.close()
g = len(lista) - 1
while g >= 0:
  print(lista[g],end='')
  g -= 1
