text = "ser o no ser"
swap = 4


def encode(text, s):
    #Inicializa el valor string
    crypt = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            #ord() regresa el valor unicode, el esl contrario al metodo char
            crypt += chr((ord(char) + s - 65) % 26 + 65)
        elif(char == " "):

            #Evita que lea el valor unicode de un espacio y lo pon
            crypt += " "
        else:
            crypt += chr((ord(char) + s - 97) % 26 + 97)

    #Transforma en minuscula
    return crypt.lower()




def main():
    print("texto: "+text)
    print("Decode: ")
    print(encode(text,swap))
main()
