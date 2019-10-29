import unicodedata
import matplotlib.pyplot as plt
import numpy as np

def obtenerTexto(archivo):
    entrada = open(archivo, 'r')
    lineas = entrada.readlines()
    lineas2 = []

    temporalList = []
    for linea in lineas:
        x = linea.split('\n')
#        print(x[0])
        p = str(unicodedata.normalize('NFKD', x[0]).encode('ascii', 'ignore'))
        #print(p[0])
        #print(p)
        o = list(p)
        o.remove(o[0])
        o.remove(o[0])
        temporalList = temporalList + o

        if ' ' in temporalList:
            temporalList.remove(' ')

    for i in range(len(temporalList)):
        uuu = temporalList[i]
        uuu = str.lower(uuu)
        #print(uuu)
        temporalList[i] = uuu
    #print(temporalList)
    return temporalList


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
                    if ';' in letras:
                        letras.remove(';')
                    if '/' in letras:
                        letras.remove('/')
                    if '?' in letras:
                        letras.remove('?')
                    if '?' in letras:
                        letras.remove('?')

                    for k in letras:
                        h = k.lower()
                        if (h.isalpha()):
                            letrasDepuradas.append(h)

    #print(letrasDepuradas)
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
    textoGeneral = {}
    
    texto1 = obtenerTexto('Text1.txt')
    texto2 = obtenerTexto('Text2.txt')
    texto3 = obtenerTexto('Text3.txt')
    texto1_letras = frecuenciaLetras(texto1)
    texto2_letras = frecuenciaLetras(texto2)
    texto3_letras = frecuenciaLetras(texto3)

    abecedario = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    textoGeneral2 = {}

    tt = 0
    for i in range(len(abecedario)):
        #print(abecedario[i])
        ooo = abecedario[i]

        t1 = texto1_letras.get(ooo)
        t2 = texto2_letras.get(ooo)
        t3 = texto3_letras.get(ooo)
        if (t1 == None):
            t1 = 0;
        if (t2 == None):
            t2 = 0;
        if (t3 == None):
            t3 = 0;
        tt = tt + t1 + t2 + t3
        #print(tt)
    for i in range (len(abecedario)):
        #print(abecedario[i])
        ooo = abecedario[i]

        t1 = texto1_letras.get(ooo)
        t2 = texto2_letras.get(ooo)
        t3 = texto3_letras.get(ooo)

        if (t1 == None):
            t1 = 0;
        if (t2 == None):
            t2 = 0;
        if (t3 == None):
            t3 = 0;

        #print(t1)
        #print(t2)
        #print(t3)
        textoGeneral[abecedario[i]] = t1 + t2 + t3
        textoGeneral2[abecedario[i]] = 100 * (t1 + t2 + t3)/tt
    print(textoGeneral)
    print("PORCENTAJE")
    print(textoGeneral2)
    #print(textoGeneral)
    names = list(textoGeneral2.keys())
    values = list(textoGeneral2.values())
    plt.bar(range(len(abecedario)), values, tick_label = names)
    plt.show()
    plt.show()
    return textoGeneral2


def test():
    frecuencias()

test()