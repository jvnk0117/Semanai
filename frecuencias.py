import unicodedata
import matplotlib.pyplot as plt
import numpy as np

#comentario

#LEE TEXTO
def obtenerTexto(archivo):
    entrada = open(archivo, 'r', encoding="utf8")
    lineas = entrada.readlines()

    temporalList = []
    for linea in lineas:
        dividedText = linea.split('\n')
        normalizedData = str(unicodedata.normalize('NFKD', dividedText[0]).encode('ascii', 'ignore'))
        normalizedDataList = list(normalizedData)
        normalizedDataList.remove(normalizedDataList[0])
        normalizedDataList.remove(normalizedDataList[0])
        temporalList = temporalList + normalizedDataList

        if ' ' in temporalList:
            temporalList.remove(' ')

    for i in range(len(temporalList)):
        charToLowerCase = temporalList[i]
        charToLowerCase = str.lower(charToLowerCase)
        temporalList[i] = charToLowerCase
    return temporalList

#####ELIINA ELEMENTOS QUE NO PERTENECEN AL ALFABETO
def depurarLetras(texto):
    letrasDepuradas = []
    for frase in texto:
        palabras = frase.strip(' ')
        for palabra in palabras:
            plabra_list = palabra.split()
            for n in plabra_list:
                letras_list = n.split(',')
                if '' in letras_list:
                    letras_list.remove('')
                for j in letras_list:
                    letras = list(j)

                    for k in letras:
                        h = k.lower()
                        if (h.isalpha()):
                            letrasDepuradas.append(h)
    return letrasDepuradas

#####CUENTA CADA VEZ QUE APARECE UN ELEMENTO EN EL TEXTO, REGRESA DICCIONARIO DE FRECUENCIAS
def frecuenciaLetras(texto):
    frequence = {}
    listaLetras = depurarLetras(texto)
    for letra in listaLetras:
        n = listaLetras.count(letra)
        frequence[letra]=n
    return frequence



##FRECUENCIAS DE 3 TEXTTOS DISTINTOS, GRAFICA
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
    totalText = 0
    for i in range(len(abecedario)):
        charToProcess = abecedario[i]

        t1 = texto1_letras.get(charToProcess)
        t2 = texto2_letras.get(charToProcess)
        t3 = texto3_letras.get(charToProcess)
        if (t1 == None):
            t1 = 0;
        if (t2 == None):
            t2 = 0;
        if (t3 == None):
            t3 = 0;
        totalText = totalText + t1 + t2 + t3
    for i in range (len(abecedario)):
        charToProcess = abecedario[i]

        t1 = texto1_letras.get(charToProcess)
        t2 = texto2_letras.get(charToProcess)
        t3 = texto3_letras.get(charToProcess)

        if (t1 == None):
            t1 = 0;
        if (t2 == None):
            t2 = 0;
        if (t3 == None):
            t3 = 0;
        textoGeneral[abecedario[i]] = t1 + t2 + t3
        textoGeneral2[abecedario[i]] = 100 * (t1 + t2 + t3)/totalText

    #print(textoGeneral)
    #print("PORCENTAJE")
    #print(textoGeneral2)
    names = list(textoGeneral2.keys())
    values = list(textoGeneral2.values())
    plt.bar(range(len(abecedario)), values, tick_label = names)
    plt.show()
    plt.show()
    return textoGeneral2


#FRECUANCIA STRING, GRAFICA
def frecuenciaTexto(textoAnalizar):
    #print("TEXTO A ANALIZAR")

    #print(textoAnalizar)

    textoGeneral = {}


    abecedario = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    textoGeneral2 = {}
    lineas = textoAnalizar
    temporalList = []
    for linea in lineas:
        dividedText = linea.split('\n')
        #        print(x[0])
        normalizedData = str(unicodedata.normalize('NFKD', dividedText[0]).encode('ascii', 'ignore'))
        normalizedDataList = list(normalizedData)
        normalizedDataList.remove(normalizedDataList[0])
        normalizedDataList.remove(normalizedDataList[0])
        temporalList = temporalList + normalizedDataList

        if ' ' in temporalList:
            temporalList.remove(' ')

    for i in range(len(temporalList)):
        charToLowerCase = temporalList[i]
        charToLowerCase = str.lower(charToLowerCase)
        # print(uuu)
        temporalList[i] = charToLowerCase

    oooDepurada = depurarLetras(temporalList)
    totalText = 0
    texto1 = frecuenciaLetras(oooDepurada)

    for i in range(len(abecedario)):
        charToProcess = abecedario[i]
        t1 = texto1.get(charToProcess)

        if (t1 == None):
            t1 = 0
        totalText = totalText + t1
        #print(totalText)
    for i in range(len(abecedario)):
        charToProcess = abecedario[i]

        t1 = texto1.get(charToProcess)
        if (t1 == None):
            t1 = 0


        textoGeneral[abecedario[i]] = t1
        textoGeneral2[abecedario[i]] = 100 * (t1) / totalText


    ######GRAFICAR
   # names = list(textoGeneral2.keys())
   # values = list(textoGeneral2.values())
   # plt.bar(range(len(abecedario)), values, tick_label=names)
   # plt.show()
   # plt.show()
    #######GRAFICAR


    return textoGeneral2


def test():
    frecuencias()
    frecuenciaTexto("PEPE PECAS PICA PAPAS")


if __name__ == '__main__':
    test()
