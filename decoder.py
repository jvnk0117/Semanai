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
    results = []
    for i in range(1, 28):    #For cycle from the first letter to last
        decoded = encoder.encode(text, -i)
        result = 'Attempt ' +  str(i) + ' Message: ' + str(decoded)
        print(result)
        results.append(decoded)
    answer = getAnswer(results)
    print('\n\nThe right one should be: ', answer)


def getAnswer(results):
    articulos = ['el', 'la', 'los', 'las', 'este', 'esta', 'estos', 'un',
                 'una', 'unos', 'lo']
    for result in results:
        x = result.split(' ')
        for palabra in x:
            if palabra in articulos:
                return result


if __name__ == '__main__':
    decodedText = decoder()
    print(decodedText)
