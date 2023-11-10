# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.
from grafo import Grafo
from random import randint

class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais if isinstance(pais, list) else [pais]
        self.tipo = tipo

    def __str__(self):
        return (f"Nombre: {self.nombre} - Pais: {self.pais} - Tipo: {self.tipo} .")
    
mi_grafo=Grafo(dirigido=False)
diccionario={}



m_naturales=[
    Maravilla("Cataratas del Iguazú", ["Argentina","Brasil"], "natural"),
    Maravilla("Gran Barrera de Coral", "Australia", "natural"),
    Maravilla("Monte Everest", "Nepal", "natural"),
    Maravilla("Aurora Boreal", ["Varios países del norte"], "natural"),
    Maravilla("Parque Nacional Yellowstone", "Estados Unidos", "natural"),
    Maravilla("Glaciar Perito Moreno", "Argentina", "natural"),
    Maravilla("Cañón del Colorado", "Estados Unidos", "natural")
]

m_arquitectonicas=[
    Maravilla("Torre Eiffel", "Francia", "arquitectónica"),
    Maravilla("Machu Picchu", "Perú", "arquitectónica"),
    Maravilla("Coliseo Romano", "Italia", "arquitectónica"),
    Maravilla("Petra", "Jordania", "arquitectónica"),
    Maravilla("La Gran Muralla China", "China", "arquitectónica"),
    Maravilla("Catedral de Santa María del Fiore", "Italia", "arquitectónica"),
    Maravilla("Opera House de Sídney", "Australia", "arquitectónica")
]
for i in range(7):
    print(m_arquitectonicas[i].nombre)
    diccionario[m_arquitectonicas[i].nombre] = i
    diccionario[m_naturales[i].nombre] = i

#se insertan vertices naturales en el grafo
for i in m_naturales:
    mi_grafo.insert_vertice(i.nombre)

#se insertan vertices arquitectonicos en el grafo
for i in m_arquitectonicas:
    mi_grafo.insert_vertice(i.nombre)

mi_grafo.barrido()
for i in m_naturales:
    posicionA=mi_grafo.search_vertice(i.nombre)
    puntoA= mi_grafo.get_element_by_index(posicionA)
    for j in m_naturales:
        posicionB=mi_grafo.search_vertice(j.nombre)
        puntoB=mi_grafo.get_element_by_index(posicionB)
        tester=mi_grafo.is_adyacent(puntoA[0],puntoB[0])
        if puntoA != puntoB and tester==False:
            valor= randint(100,5000);
            mi_grafo.insert_arist(puntoA[0],puntoB[0],valor)

for i in m_arquitectonicas:
    posicionA=mi_grafo.search_vertice(i.nombre)
    puntoA=mi_grafo.get_element_by_index(posicionA)
    for j in m_arquitectonicas:
        posicionB=mi_grafo.search_vertice(j.nombre)
        puntoB=mi_grafo.get_element_by_index(posicionB)
        tester=mi_grafo.is_adyacent(puntoA[0],puntoB[0])
        if puntoA != puntoB and tester==False:
            valor= randint(100,5000);
            mi_grafo.insert_arist(puntoA[0],puntoB[0],valor)

#mi_grafo.barrido()

#c.
valor=mi_grafo.kruskal()

for i in valor:
    aristas=i.split(';')
    print("Arbol")
    for j in aristas:
        print(j)

#d.
paises=[]
for i in m_naturales:
    posicionA=mi_grafo.search_vertice(i.nombre)
    puntoA= mi_grafo.get_element_by_index(posicionA)
    for j in m_arquitectonicas:
        posicionB=mi_grafo.search_vertice(j.nombre)
        puntoB=mi_grafo.get_element_by_index(posicionB)
        id_A=diccionario[puntoA[0]]
        id_B=diccionario[puntoB[0]]
        if 
