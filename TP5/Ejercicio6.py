# Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
# miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:


from arbol_binario import BinaryTree, get_value_from_file

file_jedi = open("TP5/jedis.txt")
read_lines = file_jedi.readlines()
file_jedi.close()

# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
arbol = BinaryTree()
nombre_arbol = BinaryTree()
especie_arbol = BinaryTree()
ranking_arbol = BinaryTree()

read_lines.pop(0)


# for que recorre el archivo, al ver ';' corta la linea, luego inserta nodo en los respectivo arboles
# enumerate se utiliza para iterar sobre una secuencia(lista,tupla o cadena)
for index, linea_jedi in enumerate(read_lines):
    # split separa la tira de strings en una lista de varios elementos
    jedi = linea_jedi.split(';')
    jedi.pop()
    nombre_arbol.insert_node(jedi[0], index+2)
    especie_arbol.insert_node(jedi[2], index+2)
    ranking_arbol.insert_node(jedi[1], index+2)


# b. realizar un barrido inorden del árbol por nombre y ranking;
def barrido_inorden():
    print()
    print('ARBOL NOMBRE:')
    print()
    nombre_arbol.inorden()
    print()
    print('ARBOL RANKING:')
    ranking_arbol.inorden()
    print()

# c. realizar un barrido por nivel de los árboles por ranking y especie;


def barrido_by_level():
    print('BY_LEVEL RANKING:')
    ranking_arbol.by_level()
    print()
    print('ESPECIE BY_LEVEL:')
    especie_arbol.by_level()


# d. mostrar toda la información de Yoda y Luke Skywalker;
def mostrar_info():
    valor = nombre_arbol.search('yoda')
    info = get_value_from_file("TP5/jedis.txt", valor.other_values)
    print('Información de Yoda: ')
    print(info)
    valor = nombre_arbol.search('luke skywalker')
    info = get_value_from_file("TP5/jedis.txt", valor.other_values)
    print('Informacion de Luke Skywalker: ')
    print(info)
    print()

# e. mostrar todos los Jedi con ranking “Jedi Master”;


def jedis_master(arbol, valor):
    print("Jedis con ranking Jedi Master: ")
    print()
    arbol.jedi_master(valor)

# f. listar todos los Jedi que utilizaron sabe de luz color verde;


def listar_jedi_sableverde(archivo, color):
    print()
    print('Jedis con sable de color verde: ')
    print()
    nombre_arbol.inorden_file_lightsaber(archivo, color)
    print()

# g. listar todos los Jedi cuyos maestros están en el archivo;


def mostrar_maestos(nombre_arbol):
    print('Jedis con maestros: ')
    nombre_arbol.maestros('TP5/jedis.txt')
    print()


barrido_inorden()
barrido_by_level()
mostrar_info()
jedis_master(ranking_arbol, 'jedi master')
listar_jedi_sableverde("TP5/jedis.txt", 'green')
mostrar_maestos(nombre_arbol)
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
print('Jedis de especie Togruta o Cerean:')
nombre_arbol.Togruta_o_Cerean('TP5/jedis.txt')
print()
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
print('Jedis que empiezan con A o tienen - en su nombre: ')
nombre_arbol.nombresAoGuion('TP5/jedis.txt')
