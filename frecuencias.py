import matplot

def obtenerTexto(archivo):
    entrada = open(archivo,'r')
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
    print(frequence)
    return frequence






def frecuencias():
    texto1 = obtenerTexto('Text1.txt')
    texto2 = obtenerTexto('Text2.txt')
    texto3 = obtenerTexto('Text3.txt')
    texto1_letras = frecuenciaLetras(texto1)
    texto2_letras = frecuenciaLetras(texto2)
    texto3_letras = frecuenciaLetras(texto3)



def graph():
    frecuencias()

graph()