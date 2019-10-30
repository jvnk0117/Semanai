
def encode(text, s):
    #leer un archivo como string

    print(text)
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
            crypt += chr((ord(char) + s - 97) % 26 + 97)

    #Transforma en minuscula
    return crypt.lower()

if __name__ == '__main__':

    texto = "¿Cómo es que los países - y sus habitantes - se vuelven afluentes y prósperos? Esa es una pregunta que concierne a la mayoría del mundo, pero es una pregunta que el pueblo estadounidense ha sabido resolver.Los Estados Unidos es el país más próspero en la historia del mundo. Por ejemplo, este año, nuestro producto interno bruto superará los $ 21 billones, rebasando por $ 7 billones al segundo país más grande del mundo. Este enorme rendimiento económico se traduce en uno de los niveles de vida más altos del mundo, que gozan millones de estadounidenses.Ese éxito económico significa que los estadounidenses disfrutan de un nivel de vida mucho más alto, en promedio, que las personas de todo el mundo. Experimentamos eso en todo, desde la calidad de la vivienda, hasta la abundancia y el bajo costo de los alimentos, hasta nuestro acceso a la información, la facilidad de transporte y la disponibilidad de nuevas tecnologías.A pesar del éxito de nuestro modelo económico, hay esos que continúan cuestionando si el mercado libre, los derechos de propiedad privada, el gobierno limitado y el compromiso con el estado de derecho son las claves para generar oportunidades económicas.Por cierto, es apropiado tener esa discusión. A medida que el mundo cambia, debemos considerar si nuestras leyes y nuestro sistema económico optimizan y mejoran nuestra sociedad. Algunos han pedido que Estados Unidos adopte las mismas estrategias utilizadas por otros países, centralizar más control y poder en el gobierno federal y avanzar políticas de índole socialistas.Pero cuando miramos más allá de nuestras fronteras, podemos ver que los mercados libres y el comercio ampliado han funcionado en todo el mundo. Según el Banco Mundial, por ejemplo, el 44% del mundo vivía en la pobreza extrema en 1981, subsistiendo con $1.90 por día o menos.Para 2015, esa cifra había caído a solo el 10%. En esos 35 años, más de mil millones de personas salieron de la pobreza extrema y mejoraron sus vidas.Ese progreso extraordinario se produjo con la caída del Telón de Acero y a medida que los gobiernos de todo el mundo adoptaron los mercados libres y el comercio abierto en lugar del control gubernamental como la forma más efectiva de crear oportunidades económicas.Al levantar el yugo de los impuestos confiscatorios y la planificación central, y permitir que millones de personas comiencen a tomar decisiones por sí mismas, las naciones han aprendido lo que los Estados Unidos descubrieron hace cientos de años.Bill Gates, de Microsoft, se encuentra entre los que han señalado que las personas en todo el mundo no solo se están volviendo más prósperas, sino que también están obteniendo ganancias de muchas otras maneras. Las tasas de alfabetización, educación, mortalidad infantil, tasas de vacunación están mejorando dramáticamente.Obviamente, todavía hay un largo camino por recorrer antes de que el mundo entero sea próspero, pero aquellos que se centran solo en lo negativo, o que actúan como si el mundo realmente se estuviera empobreciendo, simplemente están equivocados.Y el progreso que estamos haciendo es más importante para las personas más pobres del mundo. Por su bien, debemos rechazar mensajes engañosos sobre la necesidad de ampliar el control estatal y las barreras comerciales.En las próximas décadas, debemos esperar que miles de millones de personas continúen mejorando sus vidas. Al adoptar reformas pro-mercado, es posible. Si los trabajadores retienen los frutos de su trabajo, en lugar de verlo consumido por el gobierno; si los derechos de propiedad privada están protegidos; si el gobierno es limitado y transparente; y si los países evitan las onerosas barreras comerciales que impiden que las personas compren y vendan como elijan, si se siguen adoptando reformas como estas en todo el mundo, estos números alentadores continuarán mejorando.La elección es nuestra"
    print(encode(texto, 6))