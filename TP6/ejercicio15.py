from grafo import Grafo
from random import randint
# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.


class Maravilla:
    def __init__(self, name, country, types):
        self.name = name
        self.country = country if isinstance(country, list) else [country]
        self.types = types

    def add_pais(self, pais):
        self.country.append(pais)

    def __str__(self):
        return f"Nombre: {self.name}\nPaíses: {', '.join(self.country)}\nTipo: {self.types}"


maravillas_naturales = [
    Maravilla("Cataratas del Iguazú", ["Argentina", "Brasil"], "natural"),
    Maravilla("Gran Cañón", "Estados Unidos", "natural"),
    Maravilla("Gran Barrera de Coral", "Australia", "natural"),
    Maravilla("Aurora Boreal", ["Varios lugares del Ártico"], "natural"),
    Maravilla("Monte Everest", ["Nepal", "Tíbet"], "natural"),
    Maravilla("Parque Nacional de Yellowstone", "Estados Unidos", "natural")
]

maravillas_arquitectonicas = [
    Maravilla("Gran Pirámide de Guiza", "Egipto", "arquitectónica"),
    Maravilla("Gran Muralla China", "China", "arquitectónica"),
    Maravilla("Taj Mahal", "India", "arquitectónica"),
    Maravilla("Estatua de la Libertad", "Estados Unidos", "arquitectónica"),
    Maravilla("Coliseo Romano", "Italia", "arquitectónica"),
    Maravilla("Ciudad de Petra", "Jordania", "arquitectónica")
]
grafo = Grafo(dirigido=False)

for i in maravillas_arquitectonicas:
    grafo.insert_vertice(i, "name")

for i in maravillas_naturales:
    grafo.insert_vertice(i, "name")

for i in maravillas_naturales:
    for j in maravillas_naturales:
        positiona = grafo.search_vertice(i.name, "name")
        pointa = grafo.get_element_by_index(positiona)
        positionb = grafo.search_vertice(j.name, "name")
        pointb = grafo.get_element_by_index(positionb)
        checker = grafo.is_adyacent_criterio(
            pointa[0].name, pointb[0].name, criterio="name")
        if pointa[0].name != pointb[0].name and checker == False:
            value = randint(100, 5000)
            grafo.insert_arist(pointa[0].name, pointb[0].name, str(value), criterio_vertice="name")

for i in maravillas_arquitectonicas:
    for j in maravillas_arquitectonicas:
        positiona = grafo.search_vertice(i.name, "name")
        pointa = grafo.get_element_by_index(positiona)
        positionb = grafo.search_vertice(j.name, "name")
        pointb = grafo.get_element_by_index(positionb)
        checker = grafo.is_adyacent_criterio(
            pointa[0].name, pointb[0].name, criterio="name")
        if pointa[0].name != pointb[0].name and checker == False:
            value = randint(100, 5000)
            grafo.insert_arist(pointa[0].name, pointb[0].name, str(value), criterio_vertice="name")


#FALTA PUNTO C PORQUE NO ANDA dijkstra
#grafo.barrido()
for i in maravillas_naturales:
    positiona = grafo.search_vertice(i.name, "name")
    pointa = grafo.get_element_by_index(positiona)
    for j in maravillas_arquitectonicas:
        positionb = grafo.search_vertice(j.name, "name")
        pointb = grafo.get_element_by_index(positionb)


