from arbol_binario import BinaryTree
# Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas
# a un archivo que contiene personajes de la saga de Star Wars, de los cuales se sabe su nombre,
# altura y peso. Además deberá contemplar los siguientes requerimientos:
# a. en el árbol se almacenara solo el nombre del personaje, además de la posición en la que se
# encuentra en el archivo (nrr);
# b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo
# de baja;
# c. mostrar toda la información de Yoda y Boba Fett;
# d. mostrar un listado ordenado alfabéticamente de los personajes que miden más de 1 metro;

# e. mostrar un listado ordenado alfabéticamente de los personajes que pesan menos de 75 ki-
# los;

# f. deberá utilizar el TDA archivo desarrollado en el capítulo V;
class PersonajeStarWars:
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

    def __str__(self):
        return f"Nombre: {self.nombre} - Altura: {self.altura} cm - Peso: {self.peso} kg"
    
personajes_star_wars = [
    PersonajeStarWars("Luke Skywalker", 172, 77),
    PersonajeStarWars("Leia Organa", 150, 49),
    PersonajeStarWars("Darth Vader", 203, 136),
    PersonajeStarWars("Yoda", 66, 17),
    PersonajeStarWars("Obi-Wan Kenobi", 182, 77),
    PersonajeStarWars("Han Solo", 180, 80),
    PersonajeStarWars("Princesa Amidala", 165, 45),
    PersonajeStarWars("Chewbacca", 228, 112),
    PersonajeStarWars("R2-D2", 96, 32),
    PersonajeStarWars("C-3PO", 171, 75)
]
arbol= BinaryTree()

for i in personajes_star_wars:
    arbol.insert_node(i.nombre,i)

# arbol.inorden()

def add_character(arbol,nombre,altura,peso):
    Personaje=PersonajeStarWars(nombre,altura,peso)
    personajes_star_wars.append(Personaje)
    arbol.insert_node(Personaje.nombre,Personaje)


def modificar_personaje(arbol,value,new_value,parameter):
    if parameter== "nombre":
        arbol.update_value_for_name(value,"nombre",new_value)
        arbol.update_key(value,new_value)
    else:
        arbol.update_value(value,parameter,new_value)
    

def baja_personaje(arbol,nombre):
    arbol.delete_node(nombre)


modificar_personaje(arbol,"Mini Yoda","Mini Yodita","nombre")
add_character(arbol,"Mini Yoda",150,20)
arbol.inorden()
baja_personaje(arbol,"Princesa Amidala")
arbol.inorden()
yoda=arbol.search("Yoda")
bobafett=arbol.search("Boba Fett")

if yoda!=None:
    print(yoda.other_values)

if bobafett!=None:
    print(bobafett.other_values)
else:
    print('Boba Fett no se encontró en el arbol')

print('YEDIS QUE MIDEN MAS DE 1 METRO: ')

alturayedi=arbol.altura_yedi()
#print(alturayedi)
for i in alturayedi:
     print(i)

pesoyedi= arbol.peso_yedi()
print("YEDIS QUE PESAN MENOS DE 75:")
for i in pesoyedi:
    print(i)