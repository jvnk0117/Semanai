#Dado el mensaje obtener todas las combinaciones posibles.
#Obtener cada frecuencia de todas las configuraciones
#calcular la ji cuadrada:

# frecuencia de cada combinacion posible.
x1 = 0
# frecuencia esperada.
e0 = 0
# Ji cuadrada
j2= ((x1-e0)*(x1-e0))/e0
#Se calcula la menor ji cuadrada y esa es la frecuencia del mensaje correcto.
#Desencriptar el mensaje con esa frecuencia.

import encoder

def bruteForce():
    textInput = input("Enter the coded message\n"
                      "WARNING! This may take a while to finish\n"
                      "Message: ")
    for i in range(1, 27):
        output = encoder.encode(textInput, i)
        if(output == textInput):
            print("ATTEMPT %i: %s (INITIAL VALUE)3" % (i, output))
        else:
            print("ATTEMPT %i: %s " %(i, output))