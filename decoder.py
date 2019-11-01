import frecuencias
import encoder



def decoder(toDecode):
    # diccionarios de frecuencias
    dicFrecTDecode = frecuencias.frecuenciaTexto(toDecode)
    dicSample = frecuencias.frecuencias()
    # sacamos el maximo valor de cada diccionario ascii
    indexToDecod = ord(max(dicFrecTDecode, key=dicFrecTDecode.get))
    indexSample = ord(max(dicSample, key=dicSample.get))
    # La diferencia de los dos maximos valores es el swap.
    deltaIndex = indexToDecod - indexSample
    #LLamamos a enocoder para mover el texto con el swap degativo.
    decoded = encoder.encode(toDecode,-deltaIndex)
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
