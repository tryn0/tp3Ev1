import feedparser

abc=feedparser.parse('https://www.abc.es/rss/feeds/abc_EspanaEspana.xml')
veinte=feedparser.parse('https://www.20minutos.es/rss/')
rtve=feedparser.parse('http://api2.rtve.es/rss/temas_espana.xml')
noticias_abc = abc['entries'][:10]
noticias_veinte = veinte['entries'][:10]
noticias_rtve = rtve['entries'][:10]
noticias={'20m':noticias_veinte,'rtve':noticias_rtve,'abc':noticias_abc}

listaN = ['abc','rtve','20m', '20min','20minutos']

print("Noticiario: ['abc' - 'rtve' - '20m']? ",end="")
entry=input()
while entry:
    entry2=entry.lower()
    if entry2 not in listaN:
      entry2='20m'
    if entry2 == '20minutos' or entry2 == '20min':
      entry2='20m'
    print(" ***  T I T U L A R E S   " + entry2.upper() + "   ***")
    for a in noticias[entry2]:
      print(" --- " + a.title + " --- ")
    print("Noticiario: ['abc' - 'rtve' - '20m']? ",end="")
    entry=input()
    if entry2=="":
      print("Saliendo...")
      break