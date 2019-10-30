import frecuencias
def identificarIndice(toDecode):
    dicToDecode = frecuencias.frecuenciaTexto(toDecode)  # Se llama al metodo para obtener el diccionario con las letras  mas utilizadas en la frase.
    indiceMayorToDecode = 0
    letraToDecode = ""
    # Se calcula el mayor indice
    for x in dicToDecode.values():
        if x >= indiceMayorToDecode:
            indiceMayorToDecode = x

    # Se calcula la letra.
    letraToDecode = [key for key,indx in dicToDecode.items() if indx == indiceMayorToDecode]

    #Se calcula el char de la letra para comparar con el otro texto.
    indice = ord(letraToDecode[0])

    return indice

def identificarMenor(dicJI):
    menorJi = MAX


