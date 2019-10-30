#Dado el mensaje obtener todas las combinaciones posibles.
#Obtener cada frecuencia de todas las configuraciones
#calcular la ji cuadrada:
#Se calcula la menor ji cuadrada y esa es la frecuencia del mensaje correcto.
#Desencriptar el mensaje con esa frecuencia.

import encoder
import frecuencias

dicJI = {}

def bruteForce():
    textInput = input("Enter the coded message\n"
                      "WARNING! This may take a while to finish\n"
                      "Message: ")
    for i in range(1, 27):
        output = encoder.encode(textInput, i)
        if(output == textInput):
            print("ATTEMPT %i: %s (INITIAL VALUE)" % (i, output))
        else:
            print("ATTEMPT %i: %s " %(i, output))