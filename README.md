# BookBot 

BookBot es una herramienta simple que analiza libros de texto y proporciona estadísticas sobre el contenido.

## ¿Qué hace?

BookBot lee un archivo de texto y te muestra:
- **Conteo de palabras**: Cuántas palabras hay en total
- **Conteo de caracteres**: Frecuencia de cada letra del alfabeto (ordenada de mayor a menor)

## Instalación

1. Clona o descarga este repositorio
2. Asegúrate de tener Python 3 instalado
3. No se requieren dependencias adicionales

## Uso

```bash
python3 main.py <ruta_al_archivo_de_texto>
```

### Ejemplo:
```bash
python3 main.py books/frankenstein.txt
```

## Estructura del proyecto

```
bookbot/
├── main.py        # Archivo principal
├── stats.py       # Funciones de análisis
├── books/         # Directorio para tus libros (gitignore)
└── README.md
```

## Ejemplo de salida

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
h: 19725
...
============= END ===============
```

## Notas

- Solo analiza caracteres alfabéticos (ignora números y símbolos)
- El análisis no distingue entre mayúsculas y minúsculas
- Coloca tus archivos de texto en el directorio `books/` para mantener el proyecto organizado

---

BookBot is my first [Boot.dev](https://www.boot.dev) project!