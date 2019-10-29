import identificarIndice
import encoder

def decoder(toDecode,sampleText):
    textIdiom = open(sampleText,"r") #abrir txt de idioma.
    # sacar indices mas altos.
    indexToDecode = identificarIndice.identificarIndice(toDecode)
    indexIdiom = identificarIndice.identificarIndice(textIdiom)
    deltaIndex = int(indexIdiom) - int(indexToDecode)
    decoded = encoder.encode(toDecode,-deltaIndex)
    textIdiom.close()

    return decoded