import feedparser

#Defino los valores para luego usarlos más cómodamente#
abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veinte=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')
noticias_abc = abc['entries'][:10]
noticias_veinte = veinte['entries'][:10]
noticias_rtve = rtve['entries'][:10]

#Imprime solo las 10 primeras noticias que tú elijas, si en nigún momento no pones nada y le das intro, intentas poner algún noticiario que no está predefinido#
#o te equivocas empezará a contar 4 inputs, después de los 4 inputs, ya estén bien o no terminará el script a través de un break#
#Lo hice así para que puedas consultar infinitamente (o actualizar) y si quieres salir haciendo break con darle a intro sin poner nada sales#

v=0
while v < 1:
    print("Noticiario: ",end="")
    entry=input()
    entry2=entry.lower()
    if entry2=="":
        v+=1
    else:
        if entry2 == "abc":
            b=0
            while b <= 10:
                print(" --- " + noticias_abc[b].title + " --- ")
                if b == 9:
                    break
                    v+=1
                else:
                    b+=1
        else:
            if entry2=="rtve":
                x=0
                while x <=10:
                    print(" --- " + noticias_rtve[x].title + " --- ")
                    if x ==9:
                        break
                        v+=1
                    else:
                        x+=1
            else:
                if entry2!=" " and entry2=="20m" or "20min" or "20minutos":
                    k=0
                    while k <=10:
                        print(" --- " + noticias_veinte[k].title + " --- ")
                        if k ==9:
                            break
                            v+=1
                        else:
                            k+=1
                else:
                    v+=1