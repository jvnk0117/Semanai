import frecuencias as f

#print("swap: "+ s)


def encode(text, s):
    crypt = ""
    for i in range(len(text)):
        char = text[i]


        if (char.isupper()):
            crypt += chr((ord(char) + s - 65) % 26 + 65)
        elif(char == " "):
            crypt += " "
        else:
            crypt += chr((ord(char) + s - 97) % 26 + 97)

    return crypt.lower()


