# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
from grafo import Grafo
from random import uniform

mi_grafo = Grafo(dirigido=False)

habitaciones=['cocina','comedor','cochera','quincho','baño1','baño2','habitacion1','habitacion2','sala de estar','terraza','patio']

#se insertan las habitaciones en los vertices del grafo
for i in habitaciones:
    mi_grafo.insert_vertice(i)
    #print(i)

j=0
#Se busca la posicion del vertice en el grafo, se obtiene la info
for i in  habitaciones:
    posicion=mi_grafo.search_vertice(i)
    punto=mi_grafo.get_element_by_index(posicion)
    if punto[1].size()<3:
        k=0
        while j==0:
            if k>=len(habitaciones):
                j=1
            else:
                lugar = habitaciones[k]
                posicionb=mi_grafo.search_vertice(lugar)
                puntob=mi_grafo.get_element_by_index(posicionb)
                tester= mi_grafo.is_adyacent(punto[0],puntob[0])
                if puntob[1].size()<3 and punto[0] != puntob[0] and tester==False:
                    num= uniform(1,11)
                    valor= float(f"{num:.2f}")
                    mi_grafo.insert_arist(punto[0],puntob[0],valor)
                    if punto[1].size()==3:
                        j=1
                k+=1
        j=0

#se insertan aristas manualmente para cumplir condicion de que dos habitaciones tengan 5 aristas
num= uniform(1,11)
valor= float(f"{num:.2f}")
mi_grafo.insert_arist("patio","cochera",valor)
num= uniform(1,11)
valor= float(f"{num:.2f}")
mi_grafo.insert_arist("cochera","sala de estar",valor)
num= uniform(1,11)
valor= float(f"{num:.2f}")
mi_grafo.insert_arist("baño1","comedor",valor)
num= uniform(1,11)
valor= float(f"{num:.2f}")
mi_grafo.insert_arist("comedor","terraza",valor)

#se muestra el grafo con sus vertices y aristas respectivas
mi_grafo.barrido()
#Se muestra el arbol de minima expansion
arbol_min=mi_grafo.kruskal()



