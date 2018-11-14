import feedparser

#Definiendo valores#
abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veintem=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')

noticias_abc = abc['entries'][:10]
noticias_veintem = veintem['entries'][:10]
noticias_rtve = rtve['entries'][:10]


#Script seleccionador de noticiarios, te muestra las 10 noticias del noticiario seleccionado y reinicio del código, para salir: intro sin escribir nada#
#Aún no sé solucionar el problema de reiniciar el script sin acabarlo si pones otra cosa que no sea el noticiario, ejemplo escribir acb, bac, cualquier otra cosa, menos el nombre#
#pendiente de actualizar eso, he pensado en usar este script en el tkinter para elegir un noticiario y que me muestre las 10 primeras noticias de cada uno#
#He pensado en solucionar el tema de que si el usuario final pone otra cosa que no sea el nombre del noticiario que yo he predefinido poniendo unos botones#
#en vez de inputs, así el usuario final no tiene que poner nada, me quito de encima, de momento, el filtro de otras palabras en el input y me ahorro el escribir#
#los comandos (nombres) que les he dao a los noticiarios para que sepan elegirlos bien#
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
                            break
                            h+=1
                        else:
                            o+=1
                else:
                    h+=1
    else:
        break