import feedparser

#Definiendo valores#
abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veintem=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')
noticias_abc = abc['entries'][:10]
noticias_veintem = veintem['entries'][:10]
noticias_rtve = rtve['entries'][:10]


#Script#

n=0
k=0
o=0
h=0
while h<3:
    entry=input("Elige un noticiario: ")
    entry=entry.lower()
    if entry!= "" and entry == "abc":
        while n <= 10:
            print(" --- " + noticias_abc[n].title + " --- ")
            if n == 9:
                print(" ")
                break
            else:
                n+=1
        if entry!="" and entry=="20minutos" or "20m" or "20min" or "20minuto":
            while k <=10:
                print(" --- " + noticias_veintem[k].title + " --- ")
                if k == 9:
                    print(" ")
                    break
                else:
                    k+=1
        else:
            if entry!="" and entry=="rtve":
                while o <=10:
                    print(" --- " + noticias_rtve[o].title + " --- ")
                    if o == 9:
                        print(" ")
                        break
                    else:
                        o+=1
            else:
                h>=3