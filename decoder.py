import identificarIndice
import encoder

def decoder(toDecode,sampleText):
    textIdiom = open(sampleText,"r") #abrir txt de idioma.
    # sacar indices mas altos.
    indexToDecod = identificarIndice(toDecode)
    indexIdiom = identificarIndice(textIdiom)

    deltaIndex = indexIdiom - indexToDecod

    decoded = encoder(toDecode,-deltaIndex)

    textIdiom.close()

    return (decoded)
message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))