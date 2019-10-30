import identificarIndice
import encoder



def decoder():
    toDecode = open("textoEncriptado.txt", 'r', encoding="utf8")
    sampleText = open("Text2.txt", 'r', encoding="utf8")
    toDecodeString = toDecode.read()

    # sacar indices mas altos.
    indexToDecod = identificarIndice.identificarIndice(toDecodeString)
    indexIdiom = identificarIndice.identificarIndice(sampleText.read())

    deltaIndex = indexToDecod - indexIdiom
    print(deltaIndex)

    decoded = encoder.encode(toDecodeString,-deltaIndex)
    toDecode.close()
    sampleText.close()
    return (decoded)



if __name__ == '__main__':
    decodedText = decoder()
    print(decodedText)
