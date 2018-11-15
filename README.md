# tp3Ev1 - Programación

Trabajo de programación de Guillermo Pérez

## Funciones que quiero que haga el código python

-Lee las líneas del archivo frases.

-Invierte las líneas leídas de frases (Última -> primera)

-Invierte las palabras de cada línea ya invertida (A las lñineas ya invertidas se les invierte el orden de las palabras).

### Cosas usadas

El script desde sys importar argv

```python
from sys import argv
```

Función de leer las líneas incluidos los saltos

```python
.readline()
```


### Estado del invertidor de líneas y palabras

- [x] Codigo python lee el fichero frases
- [x] Invierte líneas
- [x] Invierte palabras de cada frase

### Funcionamiento

Para obtener nuestras frases invertidas tanto las líneas como las palabras dejo aquí una guía:

```
$ py invertirlineas.py frases > frasesInvertidas
$ py invertirpalabras.py frasesInvertidas > frasesYpalabrasInvertidas
```

En la primera línea de comandos ordenamos que se ejecute invertirlineas.py a través de python cogiendo los datos de frases, en este caso invirtiendolineas.py e invirtiendopalabras.py usan:
```python
from sys import argv
```
Y el resultado nos la imprime en un nuevo archivo que hemos llamado frasesInvertidas.
Seguidamente lanzamos otra vez py para que python ejecute otro script pero esta vez cogiendo los datos del archivo que se creó anteriormente, para que así se le apliquen 2 scripts sin tener que modificar los scripts para que encajen unos con otros, o si los quieres tener por separados. Le indicamos que el resultado nos lo imprima en un nuevo archivo que llamamos frasesYpalabrasInvertidas, y en este archivo como su nombre indica tendremos los datos de frases, alteradas después de pasarlo por el filtro invertirlineas.py y luego alteradas otra vez por invertirpalabras.py.



## Parte dos del trabajo

Quiero hacer un tkinter que al ejecutarlo nos salga una interfaz con una serie de botones:
-Noticias
	-Tres botnoes con las noticias, en principio las ya configuradas: RTVE, ABC y 20minutos. Clickas en la que quieras y se te abre una ventana con las últimas 10 noticias de la elegida.
	-Dentro de las noticias abajo del todo o arriba, según se vea mejor y sea más simple, un botón para atrás para volver a elegir otra noticia, otro botón para actualizar la noticia en la que estemos (Supongo que cargando otra vez la ventana con las noticias) y otro botón para salir (cerrar el tkinter)
-Enviar un mensaje si se te ocurre alguna mejora.
-Salir

### Funcionamiento

Gracias a feedparser podemos visualizar noticias a través de canales RSS.

```python
import feedparser
```


Definiendo los valores de los canales RSS, filtrando solo las entradas (entries) y cogiendo hasta el 10 y luego llamando a los valores según el input seleccionado (ABC, RTVE o 20minutos) llama a un valor u otro, según noticiario. Las imprime y reinicia el bucle, hasta que queramos salir que le damos intro sin escribir nada y corta el bucle.

### Estado del tkinter noticiero

- [ ] Tkinter creado
- [ ] Tkinter configurado
- [x] Lee las noticias
- [x] Imprime las noticias
- [x] Lee e imprime las 10 primeras noticias
- [x] Lee e imprime las 10 primeras noticias del noticiario que elijas: ABC, RTVE o 20minutos.


## Parte 2.1 del trabajo

En la clase de programación de 15/11/2018 hablamos de un archivo con argv[1], y gracias a una práctica del profesor jugamos con el archivo poniéndole un segundo argumento al archivo y se me ocurrió la idea de hacer un código ejecutado sólo a través de la línea de comandos.

### Funcionamiento del 2.1

Al contrario que el anterior, este funciona a través de la línea de comandos.

Para el archivo seleccionador-noticias.py
```python
$ py numero-noticias.py x 
```

En x ponemos un número de noticias que queramos que nos cargue.

Ejemplo:

```python
$ py numero-noticias.py 10
```
Y luego nos dejará elegir un noticiario, elegimos rtve, abc o 20minutos (este último como 20m, 20min o 20minutos), mayúsculas o no.

Ahora el siguiente código:

```python
$ py numero-noticias-noticiero.py x y
```

Teniendo en cuenta x como el número de noticias a visualizar e y como el noticiero. Ejemplo:

```python
$ py numero-noticias-noticiero.py 10 abc
```


Copyright© tryn0