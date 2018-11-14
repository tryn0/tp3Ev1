# Ejecutar:  python3 invertiCadaLinea.py file

from sys import argv

#función hecha en clase

def listaToStr(unaLista):
  st = ''
  for v in unaLista:
    st += v + ' '
  return st

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

# continuar con el código

fe = open(argv[1],'r')
linea = fe.readline().strip()
while linea != '':
  palabras = linea.split(' ')
  lineap = invertirLista(palabras)
  #print(listaToStr(lineap))
  print(" ".join(lineap))
  linea = fe.readline().strip()
fe.close()
