import feedparser
from sys import argv

abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veintem=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')

w=int(argv[1])
noticias_abc = abc['entries'][:w]
noticias_veintem = veintem['entries'][:w]
noticias_rtve = rtve['entries'][:w]

i=0
while i<3:
    entry=input("Elige un noticiero: ")
    entry2=entry.lower()
    if entry2!="":
        if entry2=="abc" or entry2=="rtve" or entry2=="20m" or entry2=="20minutos" or entry2=="20min":
            if entry2=="abc":
                n=0
                while n <= w:
                    print(" --- " + noticias_abc[n].title + " --- ")
                    if n == (w-1):
                        break
                        i+=1
                    else:
                        n+=1
            else:
                if entry2=="rtve":
                    o=0
                    while o <= w:
                        print(" --- " + noticias_rtve[o].title + " --- ")
                        if o == (w-1):
                            break
                            i+=1
                        else:
                            o+=1
                else:
                    if entry2=="20m" or entry2=="20min" or entry2=="20minutos":
                        k=0
                        while k <= w:
                            print(" --- " + noticias_veintem[k].title + " --- ")
                            if k == (w-1):
                                break
                                i+=1
                            else:
                                k+=1
        else:
            print("No ha elegido un noticiero valido.")
            i+=1
    else:
        print("Saliendo... ")
        break 