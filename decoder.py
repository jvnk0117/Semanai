import identificarIndice
import frecuencias
import encoder



def decoder(text):
    #toDecode = open("textoEncriptado.txt", 'r', encoding="utf8")
    sampleText = open("Text2.txt", 'r', encoding="utf8")
    #toDecodeString = toDecode.read()
    toDecode = text

    # sacar indices mas altos.
    indexToDecod = identificarIndice.identificarIndice(toDecode)
    indexIdiom = identificarIndice.identificarIndice(sampleText.read())

    deltaIndex = indexToDecod - indexIdiom

    decoded = encoder.encode(toDecode,-deltaIndex)
    #toDecode.close()
    sampleText.close()
    return ("Message Received: %s\nSwap Key: %i\nDecoded Message: %s" %(toDecode, deltaIndex, decoded))

def decode_BruteForce(text):
    for i in range(1, 28):    #For cycle from the first letter to last
        decoded = encoder.encode(text, -i)
        print('Attempt', i, 'Message: ', decoded)


if __name__ == '__main__':
    decodedText = decoder()
    print(decodedText)
