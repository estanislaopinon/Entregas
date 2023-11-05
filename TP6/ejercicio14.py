from grafo import Grafo
from random import uniform
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

habitaciones = ['cocina', 'comedor', 'cochera', 'quincho', 'baño1', 'baño2',
                'habitación1', 'habitación2', 'sala de estar', 'terraza', 'patio']

for i in habitaciones:
    grafo.insert_vertice(i)

# b.
j = 0

for i in habitaciones:
    position = grafo.search_vertice(i)
    point = grafo.get_element_by_index(position)
    if point[1].size() < 3:
        k = 0
        while j == 0:
            if k >= len(habitaciones):
                j = 1
            else:
                place = habitaciones[k]
                positionb = grafo.search_vertice(place)
                pointb = grafo.get_element_by_index(positionb)
                checker = grafo.is_adyacent(point[0], pointb[0])
                if pointb[1].size() < 3 and point[0] != pointb[0] and checker == False:
                    val = uniform(1, 11)
                    value = float(f"{val:.2f}")
                    grafo.insert_arist(point[0], pointb[0], str(value))
                    if point[1].size() == 3:
                        j = 1
                k += 1
        j = 0


val = uniform(1, 11)
value = float(f"{val:.2f}")
grafo.insert_arist("patio", "cochera", str(value))
val = uniform(1, 11)
value = float(f"{val:.2f}")
grafo.insert_arist("cochera", "sala de estar", str(value))
val = uniform(1, 11)
value = float(f"{val:.2f}")
grafo.insert_arist("baño1", "comedor", str(value))
val = uniform(1, 11)
value = float(f"{val:.2f}")
grafo.insert_arist("comedor", "terraza", str(value))
grafo.barrido()

minima_exp = grafo.kruskal()

min_exp = grafo.kruskal()
total_cable = 0
for i in min_exp:
    k = i.split(";")
    for j in k:
        total_cable = total_cable + float(j.split("-")[2])
print(f"Se necesitan {total_cable} metros de cable")
