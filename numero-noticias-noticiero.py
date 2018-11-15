import feedparser
from sys import argv

abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veintem=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')

#Defino el script para que funcione con el argumento 1 como un numero entero#
#Que lo defino como el numero de noticias que deseo visualizar#
#Luego defino el argumento 2 como el nombre del noticiero que quieres visualizar#
w=int(argv[1])
noticias_abc = abc['entries'][:w]
noticias_veintem = veintem['entries'][:w]
noticias_rtve = rtve['entries'][:w]

w2=argv[2]
w3=w2.lower()

if w3!="":
    if w3=="abc":
            n=0
            while n <= w:
                print(" --- " + noticias_abc[n].title + " --- ")
                if n == (w-1):
                    break
                else:
                    n+=1
    else:
        if w3=="rtve":
            o=0
            while o <= w:
                print(" --- " + noticias_rtve[o].title + " --- ")
                if o == (w-1):
                    break
                else:
                    o+=1
        else:
            if w3=="20m" or "20min" or "20minutos":
                k=0
                while k <= w:
                    print(" --- " + noticias_veintem[k].title + " --- ")
                    if k == (w-1):
                        break
                    else:
                        k+=1
            #else:
            	#if w3!="abc" or "rtve" or "20m" or "20minutos" or "20min":
            		#print("No ha elegido un noticiero valido.")
#Pongo esto ultimo como comentario porque no funciona, y no se me ocurre#
#como hacer funcionar ese filtro#