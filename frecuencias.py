import matplot

def obtenerTexto(archivo):
    entrada = open(archivo, 'r')
    lineas = entrada.readlines()
    lineas2 = []
    for linea in lineas:
        x = linea.split('\n')
        if '' in x:
            x.remove('')
        if len(x)>0:
            lineas2.append(x[0])
    return lineas2


def depurarLetras(texto):
    letrasDepuradas = []
    diccLetras = {'á':'a', 'é':"e", 'í':'i', 'ó':'o', 'ú':'u'}
    for frase in texto:
        palabras = frase.split(' ')
        for palabra in palabras:
            plabra_list = palabra.split()
            for n in plabra_list:
                letras_list = n.split(',')
                if '' in letras_list:
                    letras_list.remove('')
                for j in letras_list:
                    letras = list(j)
                    if '.' in letras:
                        letras.remove('.')
                    if ',' in letras:
                        letras.remove(',')
                    if '(' in letras:
                        letras.remove('(')
                    if ')' in letras:
                        letras.remove(')')
                    if '“' in letras:
                        letras.remove('“')
                    if '”' in letras:
                        letras.remove('”')
                    if '%' in letras:
                        letras.remove('%')
                    if '/' in letras:
                        letras.remove('/')
                    if '…' in letras:
                        letras.remove('…')
                    if 'á' in letras:
                        letras.remove('á')
                    if 'é' in letras:
                        letras.remove('é')
                    if 'í' in letras:
                        letras.remove('í')
                    if 'ó' in letras:
                        letras.remove('ó')
                    if 'ú' in letras:
                        letras.remove('ú')
                    for k in letras:
                        h = k.lower()
                        letrasDepuradas.append(h)

    return letrasDepuradas


def frecuenciaLetras(texto):
    frequence = {}
    listaLetras = depurarLetras(texto)
    for letra in listaLetras:
        n = listaLetras.count(letra)
        frequence[letra]=n
    return frequence


def frecuencias():
    texto1 = obtenerTexto('Text1.txt')
    texto2 = obtenerTexto('Text2.txt')
    texto3 = obtenerTexto('Text3.txt')
    texto1_letras = frecuenciaLetras(texto1)
    texto2_letras = frecuenciaLetras(texto2)
    texto3_letras = frecuenciaLetras(texto3)
