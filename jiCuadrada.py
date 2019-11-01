#Dado el mensaje obtener todas las combinaciones posibles.
#Obtener cada frecuencia de todas las configuraciones
#calcular la ji cuadrada:
#Se calcula la menor ji cuadrada y esa es la frecuencia del mensaje correcto.
#Desencriptar el mensaje con esa frecuencia.
import createTables
import encoder
import frecuencias
import identificarIndice
# lista para detectar
ABECEDARIO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u",
              "v", "w", "x", "y", "z"]
#Diccionario de Ji cuadrada
dicJI = {}

def computeJiSquared(aEncode):
    # diccionario con frec de muestra español.
    sampleTextDictionary = frecuencias.frecuencias()
    for i in range(1, 26):    #For cycle from the first letter to last
        encodedTextSwap = encoder.encode(aEncode, i) #recorremos  el  texto 26 veces
        ji = 0
        encodedTextDictionary = frecuencias.frecuenciaTexto(encodedTextSwap) # sacamos la frecuencia de cada movimiento

        for n in range(len(ABECEDARIO)):
            charToProcess = ABECEDARIO[n]    #de la lista de abecedario sacamos cada letra.
            #sacamos la freuencia de cada letra de ambos diccionarios:
            charEncodedText = encodedTextDictionary.get(charToProcess)
            charSampleText = sampleTextDictionary.get(charToProcess)
            # error de div entre 0.
            if charSampleText == 0:
                charSampleText = 0.0000000000000001
                #Se calcula la ji cuadrada de cada letra de cada iter.
            ji = ji + ((charEncodedText - charSampleText)*(charEncodedText - charSampleText))/charSampleText
            dicJI[i] = ji   # se agrega a diccionario de ji cuadrada donde i es el swap.
    swap = 26 - min(dicJI, key=dicJI.get)   # Se busca el menor ji cuadrado y se resta el total de iter para sacar la diferencia.
    print(createTables.createJiTable(dicJI)) # tablas
    print('\n\nThe right one should be: ', encoder.encode(aEncode,-swap), '\n\n')
    return swap
