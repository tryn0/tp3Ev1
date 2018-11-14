from sys import argv


leer = open(argv[1],'r')
lista = list()
linea = leer.readline()
while linea:
  lista.append(linea)
  linea = leer.readline()
leer.close()
n = len(lista) - 1
while n >= 0:
  print(lista[n],end='')
  n -= 1
