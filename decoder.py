import identificarIndice
import encoder

def decoder(toDecode,sampleText):
    textIdiom = open(sampleText,"r") #abrir txt de idioma.
    # sacar indices mas altos.
    indexToDecod = identificarIndice.identificarIndice(toDecode)
    indexIdiom = identificarIndice.identificarIndice(textIdiom)

    deltaIndex = indexIdiom - indexToDecod

    decoded = encoder.encode(toDecode,-deltaIndex)

    textIdiom.close()

    return (decoded)


