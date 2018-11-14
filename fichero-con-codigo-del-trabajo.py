import feedparser

abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veintem=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')
noticias_abc = abc['entries'][:10]
noticias_veintem = veintem['entries'][:10]
noticias_rtve = rtve['entries'][:10]


#Imprime solo las 10 primeras noticias que tú elijas, si en nigún momento no pones nada y le das intro, intentas poner algún noticiario que no está predefinido#
#o te equivocas empezará a contar 4 inputs, después de los 4 inputs, ya estén bien o no terminará el script a través de un break#
#Lo hice así para que puedas consultar infinitamente (o actualizar) y si quieres salir haciendo break con darle 4 veces a intro sin poner nada sales#
#No quería poner 3, por sí #
i=0
while i < 4:
    print("Elige un noticiario abc, 20minutos o rtve: ",end="")
    entry=input()
    entry2=entry.lower()
    if entry2!="abc" or "rtve" or "20m" or "20min" or "20minutos":
        i+=1
    else:
        if entry2=="":
            i+=1
        else:
            if entry2 == "abc":
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
                    k = 0
                    while k <=10:
                        print(" --- " + noticias_rtve[k].title + " --- ")
                        if k == 9:
                            break
                            i+=1
                        else:
                            k+=1
                else:
                    if entry2=="20m" or "20minutos" or "20":
                        s = 0
                        while s <=10:
                            print(" --- " + noticias_veintem[s].title + " --- ")
                            if s == 9:
                                break
                                i+=1
                            else:
                                s+=1