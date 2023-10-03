# Dada una lista con nombres de personajes de la saga de Avengers
# ordenados por nombre del superhéroes, de los cuales se conoce:
# nombre del superhéroe, nombre del personaje (puede ser vacio),
# grupo al que (perteneces puede ser vacio), año de aparición, por
# ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
# Resolver las siguientes tareas:
# a. Determinar si “Capitana Marvel” está en la lista y mostrar su
# nombre de personaje;
# b. Almacenar los superhéroes que pertenezcan al grupo
# “Guardianes de la galaxia” en una cola e indicar cuantos son.
# c. Mostrar de manera descendente los superhéroes que
# pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
# la galaxia”.
# d. Listar los superhéroes que tengan nombre de personajes cuyo
# año de aparición sea posterior a 1960.
# e. Hemos detectado que la superhéroe “Black Widow” está mal
# cargada por un error de tipeo, figura como “Vlanck Widow”,
# modifique dicho superhéroe para solucionar este problema.
# f. Dada una lista auxiliar con los siguientes personajes (‘Black
# Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
# información), agregarlos a la lista principal en el caso de no
# estar cargados.
# g. Mostrar todos los personajes que comienzan con C, P o S.
# h. Cargue al menos 20 superheroes a la lista.

from lista import Lista
from cola import Cola
lista=Lista()
lista2=Lista()
class personaje():
    def __init__(self,n_superheroe,n_personaje,grupo,año_aparicion):
        self.n_superheroe= n_superheroe
        self.n_personaje= n_personaje
        self.grupo=grupo
        self.año_aparicion=año_aparicion

    def __str__(self):
        return f'{self.n_superheroe} - {self.n_personaje} - {self.grupo} - {self.año_aparicion}'


def Personajes(lista):
    lista.insert(personaje('Vlanck Widow','Natasha Romanoff','Avengers','2010'),'n_superheroe')
    lista.insert(personaje('Capitana Marvel','Carol Danvers','Avengers','1968'),'n_superheroe')
    lista.insert(personaje('Pantera Negra','T-Challa','Avengers','1966'),'n_superheroe')
    lista.insert(personaje('Gamora','','Guardianes de la Galaxia','1975'),'n_superheroe')
    lista.insert(personaje('Ant-Man','Scott Lang','Avengers','1979'),'n_superheroe')
    lista.insert(personaje('Falcon','Sam Wilson','Avengers','1969'),'n_superheroe')
    lista.insert(personaje('Capitan America','Steve Rogers','Avengers','1941'),'n_superheroe')
    lista.insert(personaje('Groot','','Guardianes de la Galaxia','1960'),'n_superheroe')
    lista.insert(personaje('Ojo de Halcon','Clint Barton','Avengers','1964'),'n_superheroe')
    lista.insert(personaje('Hulk','Burce Banner','Avengers','1962'),'n_superheroe')
    lista.insert(personaje('Human Torch','Jonny Storm','Cuatro Fantasticos','1961'),'n_superheroe')
    lista.insert(personaje('Invisible Woman','Susan Storm','Cuatro Fantasticos','1961'),'n_superheroe')
    lista.insert(personaje('Iron Man','Tony Stark','Avengers','1963'),'n_superheroe')
    lista.insert(personaje('Mr.Fantastic','Reed Richards','Cuatro Fantasticos','1961'),'n_superheroe')
    lista.insert(personaje('Rocket Raccoon','','Guardianes de la Galaxia','1976'),'n_superheroe')
    lista.insert(personaje('Scarlet Witch','Wanda Maximoff','Avengers','1962'),'n_superheroe')
    lista.insert(personaje('Spider-Man','Peter Parker','Avengers','1962'),'n_superheroe')
    lista.insert(personaje("Loki", '', "Asgardiano", '1949'),"n_superheroe")
    lista.insert(personaje('Star-Lord','Peter Quill','Guardianes de la Galaxia','1976'),'n_superheroe')
    lista.insert(personaje('Thor','Thor Odinson','Avengers','1963'),'n_superheroe')
    lista.insert(personaje('Thing','Ben Grimm','Cuatro Fantasticos','1961'),'n_superheroe')   
    lista.insert(personaje("Black Cat", "Felicia Hardy", "Spiderman Allies", '1979'),"n_superheroe")



# f. Dada una lista auxiliar con los siguientes personajes (‘Black Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
#  información), agregarlos a la lista principal en el caso de no estar cargados.

def lista2(lista):
    lista2.insert(personaje("Loki", '', "Asgardiano", 1949),"n_superheroe")
    lista2.insert(personaje("Rocket Raccoon", "Rocket", "Guardianes de la Galaxia", 1976),"n_superheroe")
    lista2.insert(personaje("Hulk", "Bruce Banner", "Avengers", 1962),"n_superheroe")
    lista2.insert(personaje("Black Cat", "Felicia Hardy", "Spiderman Allies", 1979),"n_superheroe")

Personajes(lista)
# a. Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje;

def Capitana_Marvel(lista):
    lista.order_by(criterio='n_superheroe',reverse=False)
    for i in range(lista.size()):
        valor=lista.get_element_by_index(i)
        if 'Capitana Marvel' in valor.n_superheroe:
            print(f'{valor.n_superheroe} esta en la lista')

# b. Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son.

def guardianes_de_la_galaxia(lista):
    lista.order_by(criterio='grupo',reverse=False)
    guardianes= Cola()
    for i in range(lista.size()):
        valor=lista.get_element_by_index(i)
        if 'Guardianes de la Galaxia'in valor.grupo:
            guardianes.arrive(valor)
    
    contador=guardianes.size() 
    print(f'En la lista hay {contador} Guardianes de la Galaxia')       


# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de la galaxia”.
def cuatrofantasticos_guardianes_de_la_galaxia(lista):
    lista.order_by(criterio='grupo',reverse=True)
    print('--------------------------------------')
    print('Personajes de Guardianes de la Galaxia: ')
    print('--------------------------------------')
    for i in range(lista.size()):
        valor=lista.get_element_by_index(i)
        if'Guardianes de la Galaxia'in valor.grupo:
            print(f'{valor.n_superheroe} pertenece a {valor.grupo}')
    print('--------------------------------------')
    print('Personajes de los Cuatro fantasticos: ')
    print('--------------------------------------')
    for i in range(lista.size()):
        lista.order_by(criterio='grupo',reverse=True)
        valor=lista.get_element_by_index(i)
        if 'Cuatro Fantasticos' in valor.grupo:
            print(f'{valor.n_superheroe} pertenece a los Cuatro Fantasticos')

# d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960.

def posterior_1960(lista):
    lista.order_by(criterio='año_aparicion', reverse=False)
    for i in range(lista.size()):
        valor=lista.get_element_by_index(i)
        if valor.año_aparicion> '1960':
            print(f'{valor.n_superheroe} apareció en {valor.año_aparicion}')

# e. Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como “Vlanck Widow”, modifique dicho superhéroe para solucionar este problema.
def inetrcambio_black_widow(lista):
    indice=lista.search_r('Vlanck Widow',0, lista.size()-1,'n_superheroe')
    if indice!= None:
        nombre= lista.get_element_by_index(indice)
        nombre.n_superheroe='Black Widow'
    lista.barrido()


# g. Mostrar todos los personajes que comienzan con C, P o S.

def personaje_C_P_S(lista):
    lista.order_by(criterio='n_superheroe',reverse=False)
    for i in range(lista.size()):
        personaje=lista.get_element_by_index(i)
        if personaje.n_superheroe[0]=='C':
            print(f'La primer letra de {personaje.n_superheroe} es C')
        if personaje.n_superheroe[0]=='P':
            print(f'La primer letra de {personaje.n_superheroe} es P')
        if personaje.n_superheroe[0]=='S':
            print(f'La primer letra de {personaje.n_superheroe} es S')




Capitana_Marvel(lista)
print('--------------------------------------')
print('Cantidad de Guardianes de la Galaxia: ')
print('--------------------------------------')
guardianes_de_la_galaxia(lista)
cuatrofantasticos_guardianes_de_la_galaxia(lista)
print('-------------------------------------------------------')
print('Superheroes cuyo año de aparición es posterior a 1960: ')
print('-------------------------------------------------------')
posterior_1960(lista)
print('----------------------------------------------------------------------------------------------')
print('Black Widow esta mal cargado, se muestra como "Vlanck Widow", se modificara dicho superheroe', )
print('----------------------------------------------------------------------------------------------')
inetrcambio_black_widow(lista)

print('-------------------------------------')
print('Personajes que empiezan con C - P O S')
print('-------------------------------------')
personaje_C_P_S(lista)