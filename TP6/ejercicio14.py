from grafo import Grafo
from random import randint
# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

grafo = Grafo(dirigido=False)

habitaciones = ['cocina', 'comedor', 'cochera', 'quincho', 'baño-1', 'baño-2',
                'habitación-1', 'habitación-2', 'sala de estar', 'terraza', 'patio']

for i in habitaciones:
    grafo.insert_vertice(i)

j = 1

# for i in habitaciones[1:-1]:
#     value = randint(1, 11)
#     grafo.insert_arist(i, habitaciones[j-1], str(value))
#     value = randint(1, 11)
#     grafo.insert_arist(i, habitaciones[j+1], str(value))
#     j = j+1


i = 1

while i < len(habitaciones):
    value = randint(1, 11)
    grafo.insert_arist(habitaciones[i], habitaciones[j-1], str(value))
    if j+1 < len(habitaciones):

        value = randint(1, 11)
        grafo.insert_arist(habitaciones[i], habitaciones[j+1], str(value))

    j = j+2
    i = i+2

grafo.barrido()
