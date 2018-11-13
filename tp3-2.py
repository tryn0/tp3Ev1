from sys import argv

#Script que invierte las líneas
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

#Script que invierte las palabras
#Definiendo la función de intercambiar las palabras (invertir palabras)
def invertirLista(unaLista):
  t = len(unaLista) / 2
  n = len(unaLista) - 1
  i = 0
  while i < t:
    temp = unaLista[i]
    unaLista[i] = unaLista[n]
    unaLista[n] = temp
    i += 1
    n -= 1
  return(unaLista)

##Script para leer las líneas, convertir las líneas con .strip()
##luego .split() las separa por lo que hay dentro de ' ', en este caso 1 espacio
##Imprime las líneas uniendo las palabras con ' ', en este caso otro espacio
## y las convierte de nuevo con .strip(), seguidamente sino hay más líneas que leer
##cierra el bucle con k.close()
k = open(argv[1],'r')
linea = k.readline().strip()
while linea != '':
  palabras = linea.split(' ')
  linea2 = invertirLista(palabras)
  #print(listaToStr(lineap))
  print(" ".join(linea2))
  linea = k.readline().strip()
k.close()