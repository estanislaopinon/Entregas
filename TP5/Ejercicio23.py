from arbol_binario import BinaryTree
# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;

# [169]

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

criaturas=BinaryTree()

lista = [
    {'Criaturas':'Ceto''Derrotado por': '-'},{'Criaturas':'Cerda de Cromión''Derrotado por': 'Teseo'},
    {'Criaturas':'Tifón''Derrotado por': 'Zeus'},{'Criaturas':'Ortro''Derrotado por': 'Heracles'},
    {'Criaturas':'Equidna''Derrotado por': 'Argos Panoptes'},{'Criaturas':'Toro de Creta''Derrotado por': 'Teseo'},
    {'Criaturas':'Dino''Derrotado por': '-'},{'Criaturas':'Jabali de Calidón''Derrotado por': 'Atalanta'},
    {'Criaturas':'Pefredo''Derrotado por': '-'},{'Criaturas':'Carcinos''Derrotado por': '-'},
    {'Criaturas':'Enio''Derrotado por': '-'},{'Criaturas':'Gerión''Derrotado por': 'Heracles'},
    {'Criaturas':'Escila''Derrotado por': '-'},{'Criaturas':'Cloto''Derrotado por': '-'},
    {'Criaturas':'Caribdis''Derrotado por': '-'},{'Criaturas':'Láquesis''Derrotado por': '-'},
    {'Criaturas':'Euríale''Derrotado por': '-'},{'Criaturas':'Átropos''Derrotado por': '-'},
    {'Criaturas':'Esteno''Derrotado por': '-'},{'Criaturas':'Minotauro de Creta''Derrotado por': 'Teseo'},
    {'Criaturas':'Medusa''Derrotado por': 'Perseo'},{'Criaturas':'Harpías''Derrotado por': '-'},
    {'Criaturas':'Ladón''Derrotado por': 'Heracles'},{'Criaturas':'Argos Panoptes''Derrotado por': 'Hermes'},
    {'Criaturas':'Águila del Cáucaso''Derrotado por': '-'},{'Criaturas':'Aves del Estínfalo''Derrotado por': '-'},
    {'Criaturas':'Quimera''Derrotado por': 'Belerofonte'},{'Criaturas':'Talos''Derrotado por': 'Medea'},
    {'Criaturas':'Hidra de Lerna''Derrotado por': 'Heracles'},{'Criaturas':'Sirenas''Derrotado por': '-'},
    {'Criaturas':'León de Nemea''Derrotado por': 'Heracles'},{'Criaturas':'Pitón''Derrotado por': 'Apolo'},
    {'Criaturas':'Esfinge''Derrotado por': 'Edipo'},{'Criaturas':'Cierva de Cerinea''Derrotado por': '-'},
    {'Criaturas':'Dragón de la Cólquida''Derrotado por': '-'},{'Criaturas':'Basilisco''Derrotado por': '-'},
    {'Criaturas':'Cerbero''Derrotado por': '-'},{'Criaturas':'Jabalí de Erimanto''Derrotado por': '-'}]

for i in lista:
    criaturas.insert_node(i['Criaturas'],i['Derrotado por'],None,None)

#A
