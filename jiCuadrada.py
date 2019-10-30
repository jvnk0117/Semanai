#Dado el mensaje obtener todas las combinaciones posibles.
#Obtener cada frecuencia de todas las configuraciones
#calcular la ji cuadrada:
#Se calcula la menor ji cuadrada y esa es la frecuencia del mensaje correcto.
#Desencriptar el mensaje con esa frecuencia.

import encoder
import frecuencias

ABECEDARIO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]

dicJI = {}

def bruteForce():
    textInput = input("Enter the coded message\n"
                      "WARNING! This may take a while to finish\n"
                      "Message: ")
    for i in range(1, 27):
        output = encoder.encode(textInput, i)
        if(output == textInput):
            print("ATTEMPT %i: %s (INITIAL VALUE)" % (i, output))
        else:
            print("ATTEMPT %i: %s " %(i, output))

def computeJiSquared(encodedText, sampleText):
    for i in range(1, 26+1):    #For cycle from the first letter to last
        encodedTextDictionary = frecuencias.frecuenciaLetras(encodedText)
        sampleTextDictionary = frecuencias.frecuenciaLetras(sampleText)
        for n in range(len(ABECEDARIO)):
            charToProcess = ABECEDARIO[n]
            charEncodedText = encodedTextDictionary.get(charToProcess)
            charSampleText = sampleTextDictionary.get(charToProcess)
            ji = ((charEncodedText - charSampleText)^2)/charSampleText
            dicJI[n] = ji