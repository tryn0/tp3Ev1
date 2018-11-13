from sys import argv

def invertirLista(lista):
  t = len(lista) / 2
  n = len(lista) - 1
  i = 0
  while i < t:
    temp = lista[i]
    lista[i] = lista[n]
    lista[n] = temp
    i += 1
    n -= 1
  return(lista)

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

print(listafinal)

