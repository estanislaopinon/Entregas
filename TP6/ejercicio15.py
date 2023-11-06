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



dic = {}

#creates a dic with wonders, and charges'em in the graph
#only the wonder.name will be introduced in the graph
#if needed to use others parameters, will use the name to get an index from the dic
#then use the index to acces the data
for i in range(6):
    dic[maravillas_arquitectonicas[i].name]= i
    dic[maravillas_naturales[i].name]= i

new_graph = Grafo(dirigido=False)

for i in maravillas_arquitectonicas:
    grafo.insert_vertice(i.name)

for i in maravillas_naturales:
    grafo.insert_vertice(i.name)


#connects wonders
for i in maravillas_arquitectonicas:
    positiona = grafo.search_vertice(i.name)
    pointa = grafo.get_element_by_index(positiona)
    for j in maravillas_arquitectonicas:
        positionb = grafo.search_vertice(j.name)
        pointb = grafo.get_element_by_index(positionb)
        checker = grafo.is_adyacent(pointa[0],pointb[0]) 
        if  pointa != pointb and checker == False:
            value = randint(100,5000)
            grafo.insert_arist(pointa[0],pointb[0], value)

for i in maravillas_naturales:
    positiona = grafo.search_vertice(i.name)
    pointa = grafo.get_element_by_index(positiona)
    for j in maravillas_naturales:
        positionb = grafo.search_vertice(j.name)
        pointb = grafo.get_element_by_index(positionb)
        checker = grafo.is_adyacent(pointa[0],pointb[0]) 
        if  pointa != pointb and checker == False:
            value = randint(100,5000)
            grafo.insert_arist(pointa[0],pointb[0], value)


#checks if exists different types same country
countries = []
for i in maravillas_naturales:
    positiona = grafo.search_vertice(i.name)
    pointa = grafo.get_element_by_index(positiona)
    for j in maravillas_arquitectonicas:
        positionb = grafo.search_vertice(j.name)
        pointb = grafo.get_element_by_index(positionb)
        index_A = dic[pointa[0]]
        index_B = dic[pointb[0]]
        if maravillas_arquitectonicas[index_B].country[0] in maravillas_naturales[index_A].country:
            if (maravillas_arquitectonicas[index_B].country in countries) == False:
                countries.append(maravillas_arquitectonicas[index_B].country)

for i in countries:
    print(f"{i[0]} posee los 2 tipos de maravilla")


#checks if country has 2 or more wonders of the same type

nature_2 = []
non_nature_2 = []
for i in maravillas_arquitectonicas:
    positiona = grafo.search_vertice(i.name)
    pointa = grafo.get_element_by_index(positiona)
    for j in maravillas_arquitectonicas:
        positionb = grafo.search_vertice(j.name)
        pointb = grafo.get_element_by_index(positionb)
        index_A = dic[pointa[0]]
        index_B = dic[pointb[0]]
        for k in maravillas_arquitectonicas[index_B].country:
            for l in maravillas_arquitectonicas[index_A].country:
                if k == l and pointb[0] != pointa[0]:
                    if (k in non_nature_2) == False:
                        non_nature_2.append(k)
                 
for i in maravillas_naturales:
    positiona = grafo.search_vertice(i.name)
    pointa = grafo.get_element_by_index(positiona)
    for j in maravillas_naturales:
        positionb = grafo.search_vertice(j.name)
        pointb = grafo.get_element_by_index(positionb)
        index_A = dic[pointa[0]]
        index_B = dic[pointb[0]]
        for k in maravillas_naturales[index_B].country:
            for l in maravillas_naturales[index_A].country:
                if k == l and pointb[0] != pointa[0]:
                    if (k in nature_2) == False:
                        nature_2.append(k)

for i in nature_2:
    print(f"{i} posee 2 maravillas(naturaleza) del mismo tipo")

for i in non_nature_2:
    print(f"{i} posee 2 maravillas(arquitectura) del mismo tipo")


#maybe needed to implement something that checks the type-tree
bosque = new_graph.kruskal()
for arbol in bosque:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)

