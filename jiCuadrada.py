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


def swap27Times():
    for x in range (1,27):
        x= 0 #swap