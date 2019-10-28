import frecuencias as f

text = "Muller se la come"
swap = 4
print("texto: "+ text)

#print("swap: "+ s)


def encode(text, s):
    crypt = ""
    for i in range(len(text)):
        char = text[i]


        if (char.isupper()):
            crypt += chr((ord(char) + s - 65) % 26 + 65)
        else:
            crypt += chr((ord(char) + s - 97) % 26 + 97)

    return crypt.lower()

print(encode(text, swap))


