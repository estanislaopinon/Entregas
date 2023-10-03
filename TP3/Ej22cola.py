# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F)
# por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;

# b. mostrar los nombre de los superhéroes femeninos;

# c. mostrar los nombres de los personajes masculinos;

# d. determinar el nombre del superhéroe del personaje Scott Lang;

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from cola import Cola

cola = Cola()
cola_aux = Cola()


class MCU():
    def __init__(self, npersonaje, nheroe, genero):
        self.npersonaje = npersonaje
        self.nheroe = nheroe
        self.genero = genero


def personajes():
    cola.arrive(MCU("Tony Stark", "Iron Man", "M"))
    cola.arrive(MCU("Steve Rogers", "Capitan America", "M"))
    cola.arrive(MCU("Thor Odinson", "Thor", "M"))
    cola.arrive(MCU("Bruce Banner", "Hulk", "M"))
    cola.arrive(MCU("Clint Barton", "Ojo de Halcón", "M"))
    cola.arrive(MCU("Peter Parker", "Spider-Man", "M"))
    cola.arrive(MCU("T'Challa", "Pantera Negra", "M"))
    cola.arrive(MCU("Carol Danvers", "Capitana Marvel", "F"))
    cola.arrive(MCU("Scott Lang", "Ant-Man", "M"))
    cola.arrive(MCU("Hope van Dyne", "Wasp", "F"))
    cola.arrive(MCU("Stephen Strange", "Doctor-Strange", "M"))
    cola.arrive(MCU("Peter Quill", "Star-Lord", "M"))
    cola.arrive(MCU("Natasha Romanoff", "Balck Widow", "F"))
    cola.arrive(MCU("Wanda Maximoff", "Scarlet Witch", "F"))
    cola.arrive(MCU("Pietro Maximoff", "Quicksilver", "M"))
    cola.arrive(MCU("Sam Wilson", "Falcon", "M"))
    cola.arrive(MCU("Bucky Barnes", "Winter Soldier", "M"))


personajes()


def capitanamarvel(cola):
    while cola.size() > 0:
        if (cola.on_front().nheroe == "Capitana Marvel"):
            print("\n")
            print(
                f'El nombre de Capitana Marvel es: {cola.on_front().npersonaje}')
            break
        else:
            cola.atention()


capitanamarvel(cola)

# personajes()


def nombreheroinas(cola):
    while cola.size() > 0:
        if (cola.on_front().genero == "F"):
            print(f'{cola.on_front().nheroe}')
            cola.atention()
        else:
            cola.atention()


print("\n")
print("Los nombres de los superheroes femeninos son: ")
nombreheroinas(cola)

personajes()


def heroesmasc(cola):
    while cola.size() > 0:
        if (cola.on_front().genero == "M"):
            print(f'{cola.on_front().npersonaje}')
            cola.atention()
        else:
            cola.atention()


print("\n")
print("Los nombres de personajes masculinos son: ")
heroesmasc(cola)

personajes()


def scottlang(cola):
    while cola.size() > 0:
        if (cola.on_front().npersonaje == "Scott Lang"):
            print(
                f'El nombre del Superhoeroe Scott Lang es: {cola.on_front().nheroe}')
            break
        else:
            cola.atention()


print("\n")
scottlang(cola)

# personajes()


def mostrarS(cola):
    while cola.size() > 0:
        if ("S" in cola.on_front().npersonaje) or ("S" in cola.on_front().nheroe):
            print(
                f'{cola.on_front().npersonaje} - {cola.on_front().nheroe} - {cola.on_front().genero}')
            cola.atention()
        else:
            cola.atention()

# def check_startswith(cola):
#     while cola.size() > 0:
#         if cola.on_front().nheroe.startswith("S") == True or cola.on_front().npersonaje.startswith("S"):
#             cola_aux.arrive(cola.on_front())
#         cola.atention()

#     return cola_aux


print("\n")
print("Los personajes o heroes que empiezan con S son: ")

mostrarS(cola)
# def mostrarS():
#     cola_aux = check_startswith(cola)
#     while cola_aux.size() > 0:
#         atributos = vars(cola_aux.on_front())
#         for value in atributos.values():
#             print(value, end=", ")
#         print("\n")
#         cola_aux.atention


# mostrarS()

personajes()


def caroldanvers(cola):

    while cola.size() > 0:
        if (cola.on_front().npersonaje == "Carol Danvers"):
            print("El personaje Carol Danvers se encuentra en la cola")
            print(f'y su nombre de heroe es {cola.on_front().nheroe}')
            break
        else:
            cola.atention()


print("\n")
caroldanvers(cola)
