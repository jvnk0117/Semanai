import frecuencias
def identificarIndice(toDecode):
    dicToDecode = frecuencias.frecuenciaLetras(toDecode)  # Se llama al metodo para obtener el diccionario con las letras  mas utilizadas en la frase.
    indiceMayorToDecode = 0
    letraToDecode = ""
    # Se calcula el mayor indice
    for x in dicToDecode.values():
        if x >= indiceMayorToDecode:
            indiceMayorToDecode = x

    # Se calcula la letra.
    while letraToDecode == '':
        letraToDecode = dicToDecode.get(indiceMayorToDecode)
    #Se calcula el char de la letra para comparar con el otro texto.
    indice = ord(letraToDecode)

    return indice
