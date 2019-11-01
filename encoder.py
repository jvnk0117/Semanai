
def encode(text, s):
    #Inicializa el valor string
    crypt = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            #ord() regresa el valor unicode, el contrario al metodo char de acuerdo a los valores ASCII
            #26 ES EL NUMERO TOTAL DE LETRAS EN EL ALFABETO
            crypt += chr((ord(char) + s - 65) % 26 + 65) # El numero 65 indica el valor para la 'A'mayuscula, el cual nos sirve de
                                                         # limite para las letras mayusculas
        elif(char == " "):
            #Evita que lea el valor unicode de un espacio y lo añade directamente

            crypt += " "
        else:
            crypt += chr((ord(char) + s - 97) % 26 + 97) # El numero 97 indica el valor para la 'a' minuscula, el cual nos sirve de
                                                         # limite para las letras minusculas

    #Transforma en minuscula
    return crypt.lower()


