from lista_lista import Lista
from random import randint


# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} - ctg: {self.ct_ganados} - cbp: {self.cb_perdidas} - cbg: {self.cb_ganadas}'


class Pokemon():
    def __init__(self, nombre, tipo, nivel=1,  subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} - nivel: {self.nivel} - tipo: {self.tipo} - subtipo: {self.subtipo}'


e1 = Entrenador('Juan', randint(1, 10), 4, 20)
e2 = Entrenador('Maria', randint(1, 10), 2, 12)
e3 = Entrenador('Lucia', randint(1, 10), 16, 10)

entrenadores = [e1, e2, e3]
lista_entrenadores = Lista()


p1 = Pokemon('pikachu', 'electrico', randint(1, 20), 'ninguno')
p2 = Pokemon('lapras', 'agua', randint(1, 20), 'hielo')
p3 = Pokemon('vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('magnetón', 'electrico', randint(1, 20), 'acero')
p5 = Pokemon('chalizard', 'fuego', randint(1, 20), 'volador')
p6 = Pokemon('bulbasaur', 'planta', randint(1, 20), 'veneno')
p7 = Pokemon('gyarados', 'agua', randint(1, 20), 'volador')
p8 = Pokemon('geodud', 'roca', randint(1, 20), 'tierra')
p9 = Pokemon('gastly', 'fantasma', randint(1, 20), 'veneno')
p10 = Pokemon('jigglypuff', 'normal', randint(1, 20), 'hada')
p11 = Pokemon('wingull', 'agua', randint(1, 20), 'volador')
p12 = Pokemon('scovillain', 'fuego', randint(1, 20), 'planta')
p13 = Pokemon('terrakion', 'electrico', randint(1, 20))
p14 = Pokemon('tyrantrum', 'electrico', randint(1, 20))
pokemones = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]

for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

for pokemon in pokemones:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')

lista_entrenadores.barrido_entrenadores()
print()

# A obtener la cantidad de Pokémons de un determinado entrenador;


def cantidad_pokemones(lista_entrenadores, nombre):
    indice = lista_entrenadores.search(nombre, 'nombre')
    if indice != None:
        value = lista_entrenadores.get_element_by_index(indice)
        entrenado, sublista = value[0], value[1]
        print(f'{entrenado.nombre} tiene {sublista.size()} pokemones')
    else:
        print('El entrenador ingresado no existe')

# b. listar los entrenadores que hayan ganado más de tres torneos;


def mas_de_tres_torneos(lista_entrenadores):
    for i in range(lista_entrenadores.size()):
        value = lista_entrenadores.get_element_by_index(i)
        if value[0].ct_ganados > 3:
            print(value[0])

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;


def pokemon_mayor_nivel(lista_entrenadores):
    mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
    pos_mayor = 0

    for pos in range(1, lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(pos)[0]
        if entrenador.ct_ganados > mayor_cantidad:
            pos_mayor = pos
            mayor_cantidad = entrenador.ct_ganados

    valor = lista_entrenadores.get_element_by_index(pos_mayor)
    entrenador, sublista = valor[0], valor[1]

    if sublista.size() > 0:
        pokemon_mayor = sublista.get_element_by_index(0)
        for pos in range(1, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nivel > pokemon_mayor.nivel:
                pokemon_mayor = pokemon
    print(
        f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} con nivel {pokemon_mayor.nivel}')

# d. mostrar todos los datos de un entrenador y sus Pokémos;


def datos_entrenador_y_pokemones(lista_entrenadores, entrenador):
    indice = lista_entrenadores.search(entrenador, 'nombre')
    if indice != None:
        value = lista_entrenadores.get_element_by_index(indice)
        entrenado, sublista = value[0], value[1]
        print(f'{entrenado.nombre} posee estos pokemones')
        sublista.barrido()
    else:
        print('El entrenador ingresado no existe')

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;


def porcentaje_batallas_ganadas(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        value = lista_entrenadores.get_element_by_index(i)
        batallas = value[0].cb_ganadas + value[0].cb_perdidas
        porcentaje = batallas * 0.79
        if value[0].cb_ganadas > porcentaje:
            print(value[0])

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador


def pokemon_tipo(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        valor = lista_entrenadores.get_element_by_index(i)
        for j in range(0, valor[1].size()):
            value = valor[1].get_element_by_index(j)
            if (value.tipo == 'agua' and value.subtipo == 'volador'):
                print(
                    f'{valor[0].nombre} tiene a {value.nombre} de tipo: {value.tipo} y subtipo: {value.subtipo} ')
            elif (value.tipo == 'fuego' and value.subtipo == 'planta'):
                print(
                    f'{valor[0].nombre} tiene a {value.nombre} de tipo: {value.tipo} y subtipo: {value.subtipo} ')

# g. el promedio de nivel de los Pokémons de un determinado entrenador;


def promedio_pokemon(lista_entrenadores, buscar):
    prom = 0
    contador = 0
    indice = lista_entrenadores.search(buscar, 'nombre')
    if indice != None:
        valor = lista_entrenadores.get_element_by_index(indice)
        for i in range(0, valor[1].size()):
            value = valor[1].get_element_by_index(i)

            prom = prom + value.nivel
            contador += 1

        if contador > 0:
            resultado = prom / contador
            print(resultado)
        else:
            print('El entrenador no posee pokemones')

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;


def determinado_pokemon(lista_entrenadores, pokemon):
    for i in range(0, lista_entrenadores.size()):
        value = lista_entrenadores.get_element_by_index(i)
        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            if valor.nombre == pokemon:
                print(value[0].nombre)

# i. mostrar los entrenadores que tienen Pokémons repetidos;


def pokemonsRepetidos(lista_entrenadores):

    # 1
    entrenadores_por_pokemon = {}

    # 2
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        for pokemon in range(entrenador[1].size()):
            nombre_pokemon = entrenador[1].get_element_by_index(pokemon).nombre
            if nombre_pokemon in entrenadores_por_pokemon:
                entrenadores_por_pokemon[nombre_pokemon].append(
                    entrenador[0].nombre)
            else:
                entrenadores_por_pokemon[nombre_pokemon] = [
                    entrenador[0].nombre]
   # 3

    for nombre_pokemon, entrenador_list in entrenadores_por_pokemon.items():

        if len(entrenador_list) > 1:
            if len(entrenador_list) != len(set(entrenador_list)):
                print(f'{entrenador_list[0]} tiene mas de un {nombre_pokemon}')
            else:
                print(f'no hay pokemones repetidos')

#  j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;


def determinar_pokemones(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):

        value = lista_entrenadores.get_element_by_index(i)

        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            if valor.nombre in 'tyrantrum':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'terrakion':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'wingull':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            else:
                None

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;


def entrenadorx_pokemon_y(lista_entrenadores, nombreentrenador, nombrepokemon):
    indice = lista_entrenadores.search(nombreentrenador, 'nombre')
    if indice != None:
        value = lista_entrenadores.get_element_by_index(indice)
        entrenado, sublista = value[0], value[1]
        cont = 0
        for j in range(0, sublista.size()):
            valor = sublista.get_element_by_index(j)
            if valor.nombre in nombrepokemon:
                cont += 1
                print(f'Datos del entrenador: {entrenado}')
                print(f'Sus pokemones: {valor}')
        if cont == 0:
            print(f'No se encontro el pokemon: {nombrepokemon}')


nombre = input('Ingrese el nombre del entrenador que desea buscar: ')
cantidad_pokemones(lista_entrenadores, nombre)
print()
print('-----------------------------------------')
print('Entrenadores con mas de 3 torneos ganados')
print('-----------------------------------------')
mas_de_tres_torneos(lista_entrenadores)
print()
print('--------------------------------------------------------------')
print('Pokemon de mayor nivel del entrenador con mas torneos ganados:')
print('--------------------------------------------------------------')
pokemon_mayor_nivel(lista_entrenadores)
print()
print('------------------------------------------------------------')
entrenador = input('Ingrese el nombre del entrenador a investigar: ')
datos_entrenador_y_pokemones(lista_entrenadores, entrenador)
print()
print('----------------------------------------------------------')
print('Entrenadores con mas del 79 porciento de batallas ganadas:')
print('----------------------------------------------------------')
porcentaje_batallas_ganadas(lista_entrenadores)
print()
print('---------------------------------------------------------------')
print('Entrenadores con pokemones de tipo fuego/planta o agua/volador:')
print('---------------------------------------------------------------')
pokemon_tipo(lista_entrenadores)
print()
buscar = input(
    'Ingrese el entrenador al cual se le promediaran sus pokemones:')
print()
print(f'El promedio de los pokemones de {buscar} es: ')
promedio_pokemon(lista_entrenadores, buscar)
print()
print('----------------------------------------------------------------------')
pokemon = input('Ingrese el pokemon que desea contar entre los entrenadores: ')
print('----------------------------------------------------------------------')
print()
print(f'{pokemon} lo tienen: ')
determinado_pokemon(lista_entrenadores, pokemon)
print()
print('-------------------------------------')
print('Entrenadores con pokemones repetidos:')
print('-------------------------------------')
pokemonsRepetidos(lista_entrenadores)
print()
print('--------------------------------------------------------------')
print('Entrenadores con los pokemones Tyrantrum, Terrakion o Wingull:')
print('--------------------------------------------------------------')
determinar_pokemones(lista_entrenadores)
print()
print('--------------------------------------------------------------')
nombreentrenador = input('¿Que entrenador desea buscar?: ')
nombrepokemon = input('¿que pokemon desea buscar?: ')

entrenadorx_pokemon_y(lista_entrenadores, nombreentrenador, nombrepokemon)
