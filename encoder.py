def encode(archivo, s):
    #leer un archivo como string
    text = archivo.read().replace('\n','')

    #Inicializa el valor string
    crypt = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            #ord() regresa el valor unicode, el contrario al metodo char
            crypt += chr((ord(char) + s - 65) % 26 + 65)
        elif(char == " "):

            #Evita que lea el valor unicode de un espacio y lo pon
            crypt += " "
        else:
            crypt += chr((ord(
                char) + s - 97) % 26 + 97)

    #Transforma en minuscula

    return crypt.lower()



