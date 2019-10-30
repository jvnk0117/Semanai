import identificarIndice
import encoder as e



def decoder(toDecode,sampleText):
    # sacar indices mas altos.
    indexToDecod = identificarIndice.identificarIndice(toDecode)
    indexIdiom = identificarIndice.identificarIndice(sampleText)

    deltaIndex = indexIdiom - indexToDecod
    print(deltaIndex)
    decoded = e.encode(toDecode,-deltaIndex)

    sampleText.close()
    toDecode.close()

    return (decoded)


if __name__ == '__main__':
    textToDecode = open("Text2.txt", 'r', encoding="utf8")
    textSample = open("Text2.txt", 'r', encoding="utf8")

    decodedText = decoder(textToDecode,textSample)
    print(decodedText)
    textSample.close()
    textToDecode.close()
