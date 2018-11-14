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

Quiero hacer un tkinter que al ejecutarlo a través del teclado elegimos
el noticiario: abc, 20minutos o rtve.

Después de elegir el que se quiera visualizar nos pedirá el número de noticias que queremos ver, del 1 al 10. Y nos mostrará según lo que queremos
1, 2, 3, x noticias o del 1 al 10, o del 5 al 10, etc.

### Estado del tkinter noticiero

- [ ] Tkinter configurado
- [x] Lee las noticias
- [x] Imprime las noticias
- [x] Lee e imprime las 10 primeras noticias
- [x] Lee e imprime las 10 primeras noticias que elijas: ABC, RTVE o 20minutos.
- [ ] Imprime X noticias
- [ ] Imprime conjunto de noticias