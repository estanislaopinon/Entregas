
# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from lista import Lista

lista = Lista()


class heroes():
    def __init__(self, nombre, año, casa, biografia):

        self.nombre = nombre
        self.año = año
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return f'{self.nombre} - {self.año} - {self.casa} - {self.biografia}'


def superhéroes(lista):
    lista.insert(heroes('Wolverine', 1974, 'Marvel',
                 'Mutante con garras retráctiles y poder de regeneración, luchador incansable y miembro de los X-Men.'), "nombre")
    lista.insert(heroes('Linterna Verde', 1940, 'DC',
                 'Héroe con anillo que crea manifestaciones de energía y defiende el universo contra amenazas intergalácticas.'), "nombre")
    lista.insert(heroes('Dr. Strange', 2014, 'Marvel',
                 'Brillante cirujano convertido en hechicero maestro, protector del multiverso y manipulador del tiempo y la realidad.'), "nombre")
    lista.insert(heroes('Capitana Marvel', 2019, 'Marvel',
                 'Piloto de combate transformada en una poderosa heroína cósmica con fuerza, velocidad y energía cósmica ilimitada.'), "nombre")
    lista.insert(heroes('Mujer Maravilla', 1941, 'DC',
                 'Princesa amazona con habilidades sobrehumanas, sabia y valiente defensora de la justicia y la paz.'), "nombre")
    lista.insert(heroes('Flash', 1939, 'DC',
                 ' Velocista extraordinario con la capacidad de correr a velocidades superlumínicas y alterar el tiempo. usa armadura'), "nombre")
    lista.insert(heroes('Star-Lord', 1976, 'Marvel',
                 'Carismático piloto espacial, líder de los Guardianes de la Galaxia, experto en combate y aficionado a la música.'), "nombre")
    lista.insert(heroes('Iron Man', 1963, 'Marvel',
                 'Genio multimillonario, inventor y filántropo, protegido por una traje tecnológica de alta potencia y defensor incansable de la justicia.'), "nombre")
    lista.barrido()

# A

#funcion que ordena la lista en base al criterio nombre, realiza una busqueda de linterna verde, si lo encuentra, lo borra y se realiza un barrido para comprobar que no esta mas
def Linterna_verde(lista):
    lista.order_by(criterio="nombre")
    index = lista.search_r("Linterna Verde", 0, lista.size(), "nombre")

    if index != None:
        lista.delete("Linterna Verde", criterio="nombre")
    lista.barrido()

# B

#funcion que busca a Wolverine, si lo encuentra, se lo almacena y printea
def Año_Wolverine(lista):
    indice = lista.search_r("Wolverine", 0, lista.size()-1, 'nombre')
    if indice != None:
        año_wol = lista.get_element_by_index(indice)
        print(año_wol.año)

# C

#cambia la casa del Dr Strange, realiza una busqueda de este en la lista, si lo encuentra, se le cambia la casa y se hace un barrido demostrando Dr Strange con casa DC
def Cambio_casa(lista):
    indice = lista.search_r("Dr. Strange", 0, lista.size()-1, "nombre")
    if indice != None:
        new_house = lista.get_element_by_index(indice)
        new_house.casa = 'DC'
    lista.barrido()

# D

#Recorre la lista En caso de que el heroe en su biografia tenga la palabra armadura o traje, se lo printea diciendo que se encontraron estas palabras en su biografia 
def traje_armadura(lista):
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if 'armadura' in heroe.biografia:
            print(
                f'En la biografia de {heroe.nombre} se encontró la palabra armadura')
        elif 'traje' in heroe.biografia:
            print(
                f'En la biografia de {heroe.nombre} se encontró la palabra traje')

# E

#Recorre la lista de heroes, en caso de que su año de aparición sea menor a 1963, se muestra NOMBRE, CASA Y AÑO DE APARICION del heroe
def superheroes_antes_1963(lista):
    for i in range(lista.size()):
        superheroe = lista.get_element_by_index(i)
        if superheroe.año < 1963:
            print(
                f'{superheroe.nombre} - {superheroe.casa}- apareció en {superheroe.año}')

# F

#Se busca a Capitana Marvel y Mujer Maravilla en la lista, si se las encuentra, se muestra el nombre del heroe y la casa a la que pertenece 
def casa_capitanamarvel_y_mujermeravilla(lista):
    capitana = lista.search_r("Capitana Marvel", 0, lista.size()-1, "nombre")
    if capitana != None:
        nueva_casa = lista.get_element_by_index(capitana)
        print(f'{nueva_casa.nombre} pertenece a {nueva_casa.casa}')

    mujerM = lista.search_r("Mujer Maravilla", 0, lista.size()-1, "nombre")
    if mujerM != None:
        nueva_casa = lista.get_element_by_index(mujerM)
        print(f'{nueva_casa.nombre} pertenece a {nueva_casa.casa}')


# G
#Busca a Flash y StarLord en la lista e imprime toda su información
def informacion_Flash_Starlord(lista):
    flash = lista.search_r("Flash", 0, lista.size()-1, "nombre")
    if flash != None:
        info = lista.get_element_by_index(flash)
        print(f'{info.nombre} - {info.año} - {info.casa} - {info.biografia}')
    print()
    star = lista.search_r("Star-Lord", 0, lista.size()-1, "nombre")
    if star != None:
        info = lista.get_element_by_index(star)
        print(f'{info.nombre} - {info.año} - {info.casa} - {info.biografia}')

# H


def superheroes_B_M_S(lista):
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if heroe.nombre[0] == 'B':
            print(f'{heroe.nombre} empieza con B')
        if heroe.nombre[0] == 'M':
            print(f'{heroe.nombre} empieza con M')
        if heroe.nombre[0] == 'S':
            print(f'{heroe.nombre} empieza con S')

# I


def contador_de_casas(lista):
    contMarvel = 0
    contDC = 0
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if heroe.casa == 'Marvel':
            contMarvel += 1
        elif heroe.casa == 'DC':
            contDC += 1
    print(f'Cantidad de heroes Marvel: {contMarvel}')
    print(f'Cantidad de heroes DC: {contDC}')


print("----- Lista superheroes -----")
superhéroes(lista)
print('-------------------------')
print()
print('-------------------------')
print('Eliminación Lintera Verde')
print('-------------------------')
Linterna_verde(lista)

print()
print('-----------------------')
print('Año aparición Wolverine')
print('-----------------------')
Año_Wolverine(lista)
print()
print('--------------------------')
print('Cambio de casa Dr. Strange')
print('--------------------------')
Cambio_casa(lista)
print()
print('---------------------------------------------------------------------')
print('nombre de superheoroes con la palabra "traje o armadura" en biografia')
print('---------------------------------------------------------------------')
traje_armadura(lista)
print()
print('-----------------------------------------')
print('Superheroes que aparecieron antes de 1963')
print('-----------------------------------------')
superheroes_antes_1963(lista)
print('-----------------------------------------')
print('Casa de Capitana Marvel y Mujer Maravilla')
print('-----------------------------------------')
casa_capitanamarvel_y_mujermeravilla(lista)
print('-----------------------------')
print('Infromación Flash y Star Lord')
print('-----------------------------')
informacion_Flash_Starlord(lista)
print('-------------------------------------')
print('Superheroes que empiezan con B, M o S')
print('-------------------------------------')
superheroes_B_M_S(lista)
print('-------------------')
print('Contador de casas: ')
print('-------------------')
contador_de_casas(lista)
