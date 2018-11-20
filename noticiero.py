import feedparser


abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veintem=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')

noticias_abc = abc['entries'][:10]
noticias_veintem = veintem['entries'][:10]
noticias_rtve = rtve['entries'][:10]



i=0
while i<3:
    entry=input("Elige un noticiero: ")
    entry2=entry.lower()
    if entry2!="":
        if entry2=="abc" or entry2=="rtve" or entry2=="20m" or entry2=="20minutos" or entry2=="20min":
            if entry2=="abc":
                n=0
                while n <= 10:
                    print(" --- " + noticias_abc[n].title + " --- ")
                    if n == 9:
                        break
                        i+=1
                    else:
                        n+=1
            else:
                if entry2=="rtve":
                    o=0
                    while o <= 10:
                        print(" --- " + noticias_rtve[o].title + " --- ")
                        if o == 9:
                            break
                            i+=1
                        else:
                            o+=1
                else:
                    if entry2=="20m" or entry2=="20min" or entry2=="20minutos":
                        k=0
                        while k <= 10:
                            print(" --- " + noticias_veintem[k].title + " --- ")
                            if k == 9:
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