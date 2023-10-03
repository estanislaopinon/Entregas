# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a.Escribir una función que elimine de la cola todas las notificaciones de Facebook;

# b.Escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;

# c.Utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from cola import Cola
from pila import Pila

cola = Cola()
cola_aux = Cola()
pila = Pila()


class Smartphone():
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

# Carga de cola con notificaciones de redes sociales


def notificacion():
    cola.arrive(Smartphone(10.08, " Facebook ",
                " Hoy es el cumpleaños de Celeste Gomez¡Deseale un feliz cumpleaños!"))
    cola.arrive(Smartphone(15.05, " Twitter ",
                " Meli indicó que le gusta tu Retweet"))
    cola.arrive(Smartphone(12.12, " Instagram",
                " Mueblestrimar comenzó a seguirte"))
    cola.arrive(Smartphone(9.02, " WhatsApp ", " Los pibes: ¿Salimos hoy?"))
    cola.arrive(Smartphone(14.34, " Twitter ",
                " Juan ha twiteado: ¡Acabdo de descubrir lo poderoso que es Python para el analisis de datos!#Python #DaraScience"))
    cola.arrive(Smartphone(10.26, " Facebook ",
                " Tienes una solicitud de amistad de Luis Maidana"))
    cola.arrive(Smartphone(15.52, " Facebook ",
                " Alguien ha comentado tu foto"))
    cola.arrive(Smartphone(11.27, " Twitter ",
                " Nuevo tutorial: Introducción a la programación con Python. ¡No te lo pierdas! #Python #Programación"))
    cola.arrive(Smartphone(13.19, " Facebook ",
                " Recibiste una invitación para unirte a un grupo"))
    cola.arrive(Smartphone(12.05, " Facebook ",
                " Recuerda que tienes un evento programado para hoy"))


while cola.size() > 0:
    valor = cola.atention()
    cola_aux.arrive(valor)


notificacion()

# Función para eliminar notifiaciones de Facebook


def elimnotFacebook(cola):
    while cola.size() > 0:
        if cola.on_front().aplicacion == " Facebook ":
            cola.atention()
        else:
            print(
                f'{cola.on_front().hora}{cola.on_front().aplicacion}:{cola.on_front().mensaje}')
            cola.atention()


print("\n")
print("Notificaciones sin Facebook")
elimnotFacebook(cola)
print("\n")

# Función que muestra las notificaciones de Twitter que tienen la palabra "Python"


def notTwitterpython(cola):
    while cola.size() > 0:
        if (cola.on_front().aplicacion == " Twitter ") and ("Python" in cola.on_front().mensaje):
            print(f'{cola.on_front().mensaje}')
            cola.atention()
        else:
            cola.atention()


print("Notificaciones de Twitter con la palabra (Python)")
print("\n")
notificacion()
notTwitterpython(cola)

# función para contar la cantidad de notificaciones recibidas entre las 11:43 y las 15:57


def notificacioneshora(cola, pila):
    contnot = 0
    while cola.size() > 0:
        if cola.on_front().hora >= 11.43 and cola.on_front().hora <= 15.57:
            valor = cola.atention()
            pila.push(valor)
            contnot += 1
        else:
            cola.atention()
    return contnot


notificacion()
notificacioneshora(cola, pila)
print("\n")
print(f'Entre las 11.43 y las 15.57 llegaron {pila.size()} notificaciones')
