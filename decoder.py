import identificarIndice

def decoder(toDecode,sampleText):
    textIdiom = open(sampleText,"r") #abrir txt de idioma.
    # sacar indices mas altos.
    indexToDecod = identificarIndice(toDecode)
    indexIdiom = identificarIndice(textIdiom)

    deltaIndex = indexIdiom - indexToDecod



    textIdiom.close()



    return ("issues")