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

class Entrenador():#Se define la clase Entrenador

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} - ctg: {self.ct_ganados} - cbp: {self.cb_perdidas} - cbg: {self.cb_ganadas}'


class Pokemon():#Se define la clase Pokemon
    def __init__(self, nombre, tipo, nivel=1,  subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} - nivel: {self.nivel} - tipo: {self.tipo} - subtipo: {self.subtipo}'

#Elementos de la clase Entrenador
e1 = Entrenador('Juan', randint(1, 10), 4, 20)
e2 = Entrenador('Maria', randint(1, 10), 2, 12)
e3 = Entrenador('Lucia', randint(1, 10), 16, 10)

entrenadores = [e1, e2, e3]
lista_entrenadores = Lista()#Se declara la lista

#Elementos de la clase Pokemon
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
p15 =Pokemon('pikachu', 'electrico', randint(1, 20), 'ninguno')
pokemones = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14,p15]

for entrenador in entrenadores:#Se insertan los entenadores en la lista con el criterio nombre
    lista_entrenadores.insert(entrenador, 'nombre')

#Se insertan los pokemones en la sublista
for pokemon in pokemones:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)#se genera un numero random para obtener un entrenador
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')#se inserta en el entrenador un pokemon

lista_entrenadores.barrido_entrenadores()
print()

# a. obtener la cantidad de Pokémons de un determinado entrenador;
def cantidad_pokemones(lista_entrenadores, nombre):
    indice = lista_entrenadores.search(nombre, 'nombre')#Se busca la posicion del entrenador, retorna NONE si no se encuentra
    if indice != None:#Si es distinto de vacio
        value = lista_entrenadores.get_element_by_index(indice)#Se busca el entrenador en funcion del indice
        entrenado, sublista = value[0], value[1]#se almacenan los datos en sus respectivas variables
        print(f'{entrenado.nombre} tiene {sublista.size()} pokemones')#muestra el entrenador y sus pokemones
    else:
        print('El entrenador ingresado no existe')

# b. listar los entrenadores que hayan ganado más de tres torneos;
def mas_de_tres_torneos(lista_entrenadores):
    for i in range(lista_entrenadores.size()):#Se ejecuta por todos los entrenadores
        value = lista_entrenadores.get_element_by_index(i)#Se guarda la información en la variable value
        if value[0].ct_ganados > 3:#Si el entrenador tiene mas de 3 torneos ganados se lo printea
            print(value[0])

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def pokemon_mayor_nivel(lista_entrenadores):#se toma la lista de entrenadores
    mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados#Se almacena la cantidad de torneos ganados del 1er entrenador
    pos_mayor = 0

    for pos in range(1, lista_entrenadores.size()):#cicla por toda la lista de entrenadores
        entrenador = lista_entrenadores.get_element_by_index(pos)[0]#busca el entrenador en posicion
        if entrenador.ct_ganados > mayor_cantidad:#Si es mayor se actualizan las variables
            pos_mayor = pos
            mayor_cantidad = entrenador.ct_ganados

    valor = lista_entrenadores.get_element_by_index(pos_mayor)#Se obtiene el entrenador
    entrenador, sublista = valor[0], valor[1]#se almacenan los datos en sus respectivas variables

    if sublista.size() > 0:#Se cicla por la sublista para obtener el pokemon de mayor nivel
        pokemon_mayor = sublista.get_element_by_index(0)
        for pos in range(1, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nivel > pokemon_mayor.nivel:
                pokemon_mayor = pokemon
    print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} con nivel {pokemon_mayor.nivel}')

# d. mostrar todos los datos de un entrenador y sus Pokémos;
def datos_entrenador_y_pokemones(lista_entrenadores, entrenador):
    indice = lista_entrenadores.search(entrenador, 'nombre')#Se busca la posicion del entrenador, retorna NONE si no se encuentra
    if indice != None:
        value = lista_entrenadores.get_element_by_index(indice)#Se busca el entrenador en funcion del indice
        entrenado, sublista = value[0], value[1]#se almacenan los datos en sus respectivas variables, se lo printea y hace un barrido de pokemones
        print(f'{entrenado.nombre} posee estos pokemones')
        sublista.barrido()
    else:
        print('El entrenador ingresado no existe')

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def porcentaje_batallas_ganadas(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):#Cicla por los entrenadores, calcula su % y los imprime en caso de que sean mayor a 79
        value = lista_entrenadores.get_element_by_index(i)
        batallas = value[0].cb_ganadas + value[0].cb_perdidas
        porcentaje = batallas * 0.79
        if value[0].cb_ganadas > porcentaje:
            print(value[0])

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador

def pokemon_tipo(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):#Cicla por los entrenadores
        valor = lista_entrenadores.get_element_by_index(i)
        for j in range(0, valor[1].size()):#Cicla por los pokemones y comprueba los condicionales, en caso de serlo, printea
            value = valor[1].get_element_by_index(j)
            if (value.tipo == 'agua' and value.subtipo == 'volador'):
                print(f'{valor[0].nombre} tiene a {value.nombre} de tipo: {value.tipo} y subtipo: {value.subtipo} ')
            elif (value.tipo == 'fuego' and value.subtipo == 'planta'):
                print(f'{valor[0].nombre} tiene a {value.nombre} de tipo: {value.tipo} y subtipo: {value.subtipo} ')

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promedio_pokemon(lista_entrenadores, buscar):#Recibe un entrenador,revisa si existe, cicla por los pokemones, los suma y despues calcula su promedio e imprime
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

def determinado_pokemon(lista_entrenadores, pokemon):#Recibe un pokemon, cicla por los entrenadores y por pokemon, revisa si existen y printea en caso de existir
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

    # 2 Cicla por entrenador y pokemon, si el pokemon esta en el diccionario, se lo añade, sino lo crea
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        for pokemon in range(entrenador[1].size()):
            nombre_pokemon = entrenador[1].get_element_by_index(pokemon).nombre
            if nombre_pokemon in entrenadores_por_pokemon:
                entrenadores_por_pokemon[nombre_pokemon].append(entrenador[0].nombre)
            else:
                entrenadores_por_pokemon[nombre_pokemon] = [entrenador[0].nombre]
   # 3
    #obtiene los items del diccionario y cicla por las posibles combinaciones, en caso de un entrenador tenga dos pokemones iguales lo printea
    for nombre_pokemon, entrenador_list in entrenadores_por_pokemon.items():

        if len(entrenador_list) > 1:
            if len(entrenador_list) != len(set(entrenador_list)):
                print(f'{entrenador_list[0]} tiene mas de un {nombre_pokemon}')
            else:
                print(f'no hay pokemones repetidos')

#  j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
def determinar_pokemones(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):#cicla por la lista de entrenadores y pokemones, imprime en caso de que tenga alguno de los 3 pokemones
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
def entrenadorx_pokemon_y(lista_entrenadores, nombreentrenador, nombrepokemon):#obtiene un entrenador y un pokemon, revisa si existe el entrenador, imprime sus datos, en caso de no existir el pokemon, imprime que no se encontró
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
