import unicodedata
import matplotlib.pyplot as plt
import numpy as np


###########LEE ARCHIVOS, NORMALIZA TEXTO PARA IGUALAR ACENTOS A SU VERSION SIN ACENTO...
def obtenerTexto(archivo):
    entrada = open(archivo, 'r', encoding="utf8")
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

#########################ELIMINA ELEMENTOS QUE NO SEAN LETRAS DEL ABECEDARIO
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

    #print(letrasDepuradas)
    return letrasDepuradas

######CUENTA CUANTAS VECES APARECE CADA CARACTER EN TEXTO
def frecuenciaLetras(texto):
    frequence = {}
    listaLetras = depurarLetras(texto)
    for letra in listaLetras:
        n = listaLetras.count(letra)
        frequence[letra]=n
    #print(frequence)
    return frequence





#########CALCULA LA FRECUENCIA DE EL LENGUAJE ESPANOL, EN BASE A Text1, Text2 y Text3
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
        x = abecedario[i]

        t1 = texto1_letras.get(x)
        t2 = texto2_letras.get(x)
        t3 = texto3_letras.get(x)
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
        x = abecedario[i]

        t1 = texto1_letras.get(x)
        t2 = texto2_letras.get(x)
        t3 = texto3_letras.get(x)

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


#########CALCULA LA FRECUENCIA DE EL TEXTO, EN LENGUAJE ESPANOL
def frecuenciaTexto(textoAnalizar):
   # print("TEXTO A ANALIZAR")
   # print(textoAnalizar)

    textoGeneral = {}


    abecedario = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    textoGeneral2 = {}
    lineas = textoAnalizar
    temporalList = []
    for linea in lineas:
        x = linea.split('\n')
        #        print(x[0])
        p = str(unicodedata.normalize('NFKD', x[0]).encode('ascii', 'ignore'))
        # print(p[0])
        # print(p)
        o = list(p)
        o.remove(o[0])
        o.remove(o[0])
        temporalList = temporalList + o

        if ' ' in temporalList:
            temporalList.remove(' ')

    for i in range(len(temporalList)):
        uuu = temporalList[i]
        uuu = str.lower(uuu)
        # print(uuu)
        temporalList[i] = uuu
    #print(temporalList)

    oooDepurada = depurarLetras(temporalList)
    #print(oooDepurada)
    #print(type(oooDepurada))
    tt = 0
    texto1 = frecuenciaLetras(oooDepurada)

    for i in range(len(abecedario)):
        # print(abecedario[i])
        ooo = abecedario[i]
        t1 = texto1.get(ooo)

        if (t1 == None):
            t1 = 0
        tt = tt + t1
        # print(tt)
    for i in range(len(abecedario)):
        # print(abecedario[i])
        s = abecedario[i]

        t1 = texto1.get(ooo)
        if (t1 == None):
            t1 = 0


        #print(t1)
        #print(tt)
        # print(t2)
        # print(t3)
        textoGeneral[abecedario[i]] = t1
        textoGeneral2[abecedario[i]] = 100 * (t1) / tt
    #print(textoGeneral)
   # print("PORCENTAJE")
   # print(textoGeneral2)
    # print(textoGeneral)

    ######GRAFICAR
    names = list(textoGeneral2.keys())
    values = list(textoGeneral2.values())
    plt.bar(range(len(abecedario)), values, tick_label=names)
    plt.show()
    plt.show()
    #######GRAFICAR


    return textoGeneral2


def test():
    frecuencias()
    frecuenciaTexto("PEPE PECAS PICA PAPAS")


if __name__ == '__main__':
    test()
