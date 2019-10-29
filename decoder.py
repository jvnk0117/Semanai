import identificarIndice
import encoder
import frecuencias

def decoder(toDecode):
    # sacar indices mas altos.
    indexToDecod = frecuencias.frecuenciaLetras(toDecode)
    indexIdiom = frecuencias.frecuencias()

    deltaIndex = indexIdiom - indexToDecod

    decoded = encoder.encode(toDecode,-deltaIndex)

    return (decoded)


