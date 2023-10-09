from arbol_binario import BinaryTree
arbol = BinaryTree()
arbol_superheroes = BinaryTree()
arbol_villanos = BinaryTree()
# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:


# d. determinar cuántos superhéroes hay el árbol;

# f. listar los superhéroes ordenados de manera descendente;


# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
def carga(arbol):
    lista = [{'nombre': 'Iron Man ', 'heroe': True},
             {'nombre': 'Hombre Araña', 'heroe': True},
             {'nombre': 'Tanos ', 'heroe': False},
             {'nombre': 'Ant Man ', 'heroe': True},
             {'nombre': 'Loki', 'heroe': False},
             {'nombre': 'Capitan América', 'heroe': True},
             {'nombre': 'Dotor Strange', 'heroe': True}]

    for i in lista:
        arbol.insert_node(i['nombre'], i['heroe'])


# b. listar los villanos ordenados alfabéticamente;
def alfabeticamente(arbol):
    arbol.inorden()

# c. mostrar todos los superhéroes que empiezan con C;


def superheroes_con_C(arbol, letra, heroe):
    arbol.inorden_start_with(letra, heroe)

# d. determinar cuántos superhéroes hay el árbol;


def contador_superheroes(arbol, heroe):
    if heroe == True:
        print(
            f'La cantidad de superheroes en el arbol es: {arbol.contar_heroes(heroe)}')

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;


def correccion_heroe(arbol):
    print('')
    nombre = input('Ingrese el nombre que quiere cambiar: ')
    pos = arbol.search(nombre)
    if pos:
        heroe = pos.other_values
        arbol.delete_node(nombre)
        nuevo_nombre = input('Ingrese nuevo nombre: ')
        arbol.insert_node(nuevo_nombre, heroe)
        print('Cambio realizado exitosamente')
        arbol.inorden()
    else:
        print(f'{nombre} no esta en el arbol')

# f. listar los superhéroes ordenados de manera descendente;


def heroes_descendente(arbol):
    arbol.inorden_super_or_villano(True)


# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
def separacion_arbol(arbol_superheroes, arbol_villanos):
    arbol.separacion_de_arbol(arbol_superheroes, arbol_villanos)
    print('')
    print('Arbol de heroes: ')
    print('')
    arbol_superheroes.inorden()
    print('')
    print('Arbol de villanos: ')
    print('')
    arbol_villanos.inorden()

# I. determinar cuántos nodos tiene cada árbol;


def contador_de_nodos(arbol, heroe):
    valor = arbol.contar_heroes(heroe)
    if heroe == True:
        print(f'El arbol de Superheroes cuenta con {valor} nodos')
        print('')
    else:
        if heroe == False:
            print(f'El arbol de Villanos cuenta con {valor} nodos')
            print('')

# II. realizar un barrido ordenado alfabéticamente de cada árbol.


def barrido_orden_alfabetico(arbol, heroe):
    if heroe == True:
        print('Arbol de superheroes ordenados alfabeticamente: ')
        print('')
        arbol.inorden()
    else:
        if heroe == False:
            print('Arbol de Villanos ordenados alfabeticamente: ')
            print('')
            arbol.inorden()


carga(arbol)
alfabeticamente(arbol)
print("Superheroes que empiezan con C: ")
superheroes_con_C(arbol, "C", True)

print('')

contador_superheroes(arbol, True)
correccion_heroe(arbol)
print('')
print('Superheroes ordenados de manera descendente: ')
heroes_descendente(arbol)
print('')
print('Creación del bosque')
separacion_arbol(arbol_superheroes, arbol_villanos)
contador_de_nodos(arbol_superheroes, True)
contador_de_nodos(arbol_villanos, False)

barrido_orden_alfabetico(arbol_superheroes, True)
barrido_orden_alfabetico(arbol_villanos, False)
