import feedparser

#Definiendo valores#
abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veintem=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')
noticias_abc = abc['entries'][:10]
noticias_veintem = veintem['entries'][:10]
noticias_rtve = rtve['entries'][:10]


#Script#


h=0
while h<3:
    entry=input("Elige un noticiario: ")
    entry2=entry.lower()
    if entry2!="":
        if entry2=="abc":
            n=0
            while n <= 10:
                print(" --- " + noticias_abc[n].title + " --- ")
                if n == 9:
                    print(" ")
                    break
                    h+=1
                else:
                    n+=1
        else:
            if entry2=="rtve":
                k=0
                while k <=10:
                    print(" --- " + noticias_rtve[k].title + " --- ")
                    if k == 9:
                        print(" ")
                        break
                        h+=1
                    else:
                        k+=1
            else:
                if entry2=="20minutos" or "20m" or "20min" or "20minuto":
                    o=0
                    while o <=10:
                        print(" --- " + noticias_veintem[o].title + " --- ")
                        if o == 9:
                            print(" ")
                            break
                            h+=1
                        else:
                            o+=1
                else:
                    h+=1