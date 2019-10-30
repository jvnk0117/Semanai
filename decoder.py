import identificarIndice
import encoder as e

sampleText = open("Text2.txt", "r", encoding="utf8")  # abrir txt de idioma.


def decoder():
    sampleText = open("Text2.txt","r", encoding="utf8") #abrir txt de idioma.
    toDecode = open("Text1.txt","r", encoding="utf8") #abrir txt de idioma.
    # sacar indices mas altos.
    indexToDecod = identificarIndice.identificarIndice(toDecode)
    indexIdiom = identificarIndice.identificarIndice(sampleText)


    #Calcula el indice de la letra mas usada en el texto
    deltaIndex = indexIdiom - indexToDecod
    print(deltaIndex)
    #desencripta el mensaje de acuerdo con la letra mas concurrente en ambos textos
    decoded = e.encode(toDecode,-deltaIndex)
    #cierre de archivos
    sampleText.close()
    toDecode.close()

    return (decoded)

print(sampleText)
#print(e.encode(sampleText,4))

#if __name__ == '__main__':
    #textToDecode = open("Text2.txt", 'r', encoding="utf8")
    #textSample = open("Text2.txt", 'r', encoding="utf8")
    #text = open("Text1.txt", "r", encoding="utf8")  # abrir txt de idioma.

    #e.encode(text,4)
    #decodedText = decoder()
    #print(decodedText)
    #textSample.close()
    #textToDecode.close()
