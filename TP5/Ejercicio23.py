from arbol_binario import BinaryTree
# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

criaturas = BinaryTree()

lista = [
    {'Criaturas': 'Ceto', 'Derrotado por': '-'},
    {'Criaturas': 'Cerda de Cromión', 'Derrotado por': 'Teseo'},
    {'Criaturas': 'Tifón', 'Derrotado por': 'Zeus'},
    {'Criaturas': 'Ortro', 'Derrotado por': 'Heracles'},
    {'Criaturas': 'Equidna', 'Derrotado por': 'Argos Panoptes'},
    {'Criaturas': 'Toro de Creta', 'Derrotado por': 'Teseo'},
    {'Criaturas': 'Dino', 'Derrotado por': '-'},
    {'Criaturas': 'Jabali de Calidón', 'Derrotado por': 'Atalanta'},
    {'Criaturas': 'Pefredo', 'Derrotado por': '-'},
    {'Criaturas': 'Carcinos', 'Derrotado por': '-'},
    {'Criaturas': 'Enio', 'Derrotado por': '-'},
    {'Criaturas': 'Gerión', 'Derrotado por': 'Heracles'},
    {'Criaturas': 'Escila', 'Derrotado por': '-'},
    {'Criaturas': 'Cloto', 'Derrotado por': '-'},
    {'Criaturas': 'Caribdis', 'Derrotado por': '-'},
    {'Criaturas': 'Láquesis', 'Derrotado por': '-'},
    {'Criaturas': 'Euríale', 'Derrotado por': '-'},
    {'Criaturas': 'Átropos', 'Derrotado por': '-'},
    {'Criaturas': 'Esteno', 'Derrotado por': '-'},
    {'Criaturas': 'Minotauro de Creta', 'Derrotado por': 'Teseo'},
    {'Criaturas': 'Medusa', 'Derrotado por': 'Perseo'},
    {'Criaturas': 'Harpías', 'Derrotado por': '-'},
    {'Criaturas': 'Ladón', 'Derrotado por': 'Heracles'},
    {'Criaturas': 'Argos Panoptes', 'Derrotado por': 'Hermes'},
    {'Criaturas': 'Águila del Cáucaso', 'Derrotado por': '-'},
    {'Criaturas': 'Aves del Estínfalo', 'Derrotado por': '-'},
    {'Criaturas': 'Quimera', 'Derrotado por': 'Belerofonte'},
    {'Criaturas': 'Talos', 'Derrotado por': 'Medea'},
    {'Criaturas': 'Hidra de Lerna', 'Derrotado por': 'Heracles'},
    {'Criaturas': 'Sirenas', 'Derrotado por': '-'},
    {'Criaturas': 'León de Nemea', 'Derrotado por': 'Heracles'},
    {'Criaturas': 'Pitón', 'Derrotado por': 'Apolo'},
    {'Criaturas': 'Esfinge', 'Derrotado por': 'Edipo'},
    {'Criaturas': 'Cierva Cerinea', 'Derrotado por': '-'},
    {'Criaturas': 'Dragón de la Cólquida', 'Derrotado por': '-'},
    {'Criaturas': 'Basilisco', 'Derrotado por': '-'},
    {'Criaturas': 'Cerbero', 'Derrotado por': '-'},
    {'Criaturas': 'Jabalí de Erimanto', 'Derrotado por': '-'}]

for i in lista:
    criaturas.insert_node(i['Criaturas'], i['Derrotado por'], None, None)

# a.


def mostrar_inorden():
    print('Listado inorden de las criaturas y quienes la derrotaron: ')
    print()
    criaturas.listado_inordencriaturas()
    print()


# b.


def agregar_descripcion():
    criatura = input('Ingrese la criatura que desea buscar: ')
    print()
    descripcion = input('Ingrese la descripcion que desea agregar: ')
    value = criaturas.search(criatura)
    value.other_values3 = descripcion
    criaturas.listado_inordencriaturas()

# c.


def mostrar_infoCriaturaTalos(criaturas):
    value = criaturas.search('Talos')
    print()
    print('Información de Talos: ')
    print()
    print(
        f'Criatura: {value.value} Derrotado por: {value.other_values} Descripcion: {value.other_values3}')
    print()


mostrar_inorden()
agregar_descripcion()
mostrar_infoCriaturaTalos(criaturas)
# d.
dic_ranking = {}
print('TOP 3 Heroes o Dioses que derrotaron mayor cantidad de Criaturas: ')
print()
criaturas.inorden_ranking(dic_ranking)


def order_por(item):
    return item[1]


ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print(ordenados[1:4])

# e.


def mostrar_criaturas_derrotadas_porHeracles(criaturas):
    print()
    print('Criaturas derrotadas por Heracles: ')
    print()
    criaturas.criaturas_derrotadas_por_Heracles()

# f.


def mostrar_criaturas_no_derrotadas(criaturas):
    print()
    print('Criaturas no derrotadas:')
    print()
    criaturas.Criaturas_no_derrotadas()


# g.
print()
print('Se ha agregado el campo: "Capturados por"')
print()


# h.
def atrapados_por(criaturas):
    cerbero = criaturas.search('Cerbero')
    cerbero.fourth_value = 'Heracles'

    toro_de_creta = criaturas.search('Toro de Creta')
    toro_de_creta.fourth_value = 'Heracles'

    cierva_cerinea = criaturas.search('Cierva Cerinea')
    cierva_cerinea.fourth_value = 'Heracles'

    jabali_de_erimanto = criaturas.search('Jabalí de Erimanto')
    jabali_de_erimanto.fourth_value = 'Heracles'
    criaturas.listado_inordencriaturas()


# i.
def busqueda_por_coincidencia(criaturas):
    print()
    busqueda = input('Ingrese criatura que desea buscar: ')
    criaturas.search_by_criatura(busqueda)
    print()

# j.


def eliminar_Basilisco_Sirenas(criaturas):
    criaturas.delete_node('Basilisco')
    criaturas.delete_node('Sirenas')
    print()
    print('Se borraron Basilisco y Sirenas de la lista')
    print()


# k.
def Heracles_y_Aves_del_Estinfalo(criaturas):
    value = criaturas.search('Aves del Estínfalo')
    value.fourth_value = 'Heracles derrotó a varias'


# l.
def cambio_Ladon(criaturas):
    ladon = criaturas.search('Ladón')
    ladon.value = 'Dragón Ladón'
    print()
    print('Se cambio el nombre de Ladón por Dragón Ladón')
    print()
    criaturas.listado_inordencriaturas()


# m.realizar un listado por nivel del árbol;
def listado_by_level(criaturas):
    print()
    print('Listado by level')
    print()
    criaturas.by_level()


# n.
def mostrar_captura_heracles(criaturas):
    print()
    print('Criaturas capturadas por Heracles: ')
    print()
    criaturas.caputrados_por_Heracles()


mostrar_criaturas_derrotadas_porHeracles(criaturas)
mostrar_criaturas_no_derrotadas(criaturas)
atrapados_por(criaturas)
busqueda_por_coincidencia(criaturas)
eliminar_Basilisco_Sirenas(criaturas)
Heracles_y_Aves_del_Estinfalo(criaturas)
cambio_Ladon(criaturas)
listado_by_level(criaturas)
mostrar_captura_heracles(criaturas)
