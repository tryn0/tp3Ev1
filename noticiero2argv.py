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

if w3=="abc" or w3=="rtve" or w3=="20m" or w3=="20minutos" or w3=="20min":
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
            if w3=="20m" or w3=="20min" or w3=="20minutos":
                k=0
                while k <= w:
                    print(" --- " + noticias_veintem[k].title + " --- ")
                    if k == (w-1):
                        break
                    else:
                        k+=1
            else:
                print("No ha elegido ningun noticiero valido. ")
if w3!="abc" or w3!="rtve" or w3!="20m" or w3!="20minutos" or w3!="20min":
    q=input("Quiere elegir otro noticiero? s/n ")
    if q=="":
        print("No elegiste nada.")
    else:
    	if q=="s":
		    argv.remove(argv[1])
		    w=0
		    w3==""
		    print("Cuantas noticias? ",end='')
		    entry=int(input())
		    w=entry
		    print("Que noticiero? ABC, RTVE o 20minutos? ",end='')
		    entry2=input()
		    entry3=entry2.lower()
		    if entry3=="abc" or entry3=="rtve" or entry3=="20m" or entry3=="20min" or entry3=="20minutos":
		        if entry3=="abc":
		            w3="abc"
		            n=0
		            while n <= w:
		                print(" --- " + noticias_abc[n].title + " --- ")
		                if n == (w-1):
		                    break
		                else:
		                    n+=1
		        else:
		            if entry3=="rtve":
		                w3="rtve"
		                o=0
		                while o <= w:
		                    print(" --- " + noticias_rtve[o].title + " --- ")
		                    if o == (w-1):
		                        break
		                    else:
		                        o+=1
		            else:
		                if entry3=="20m" or w3=="20min" or w3=="20minutos":
		                    w3="20m"
		                    k=0
		                    while k <= w:
		                        print(" --- " + noticias_veintem[k].title + " --- ")
		                        if k == (w-1):
		                            break
		                        else:
		                            k+=1
		                else:
		                    print("No ha elegido ningun noticiero valido. ")           
    	else:
    		print("Saliendo... ")
