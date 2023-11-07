from arbol_binario import BinaryTree, get_value_from_file
# Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenadade los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente: 
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo; 
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–; 
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico; 
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre; 
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum; 
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 

class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __str__(self):
        tipo_str = "/".join(self.tipos)
        return f"nombre: {self.nombre}\nNúmero en la Pokédex: #{self.numero}\nTipo/Tipos: {tipo_str}"
    
arbol_nombre= BinaryTree()
arbol_numero=BinaryTree()
arbol_tipo= BinaryTree()
pokemones = [
    {'nombre':"Bulbasaur", 'numero':1, 'tipo':"Planta-Veneno"},
    {'nombre':"Charmander", 'numero':4, 'tipo':"Fuego"},
    {'nombre':"Squirtle", 'numero':7, 'tipo':"Agua"},
    {'nombre':"Pikachu", 'numero':25, 'tipo':"Eléctrico"},
    {'nombre':"Jigglypuff", 'numero':39,'tipo': "Normal-Hada"},
    {'nombre':"Gengar", 'numero':94, 'tipo':"Fantasma-Veneno"},
    {'nombre':"Snorlax", 'numero':143, 'tipo':"Normal"},
    {'nombre':"Mewtwo", 'numero':150, 'tipo':"Psíquico"},
    {'nombre':"Gyarados", 'numero':130, 'tipo':"Agua-Volador"},
    {'nombre':"Jolteon", 'numero':135, 'tipo':"Eléctrico"},
    {'nombre':"Lycanroc", 'numero':745, 'tipo':"Roca"},
    {'nombre':"Tyrantrum", 'numero':697, 'tipo':"Roca-Dragón"},
    {'nombre':"Machamp", 'numero':68, 'tipo':"Lucha"}
]

for i in pokemones:
    arbol_nombre.insert_node(i['nombre'],[i['numero'],i['tipo']])
    arbol_numero.insert_node(i['numero'],[i['nombre'],i['tipo']])
    arbol_tipo.insert_node(i['tipo'],[i['numero'],i['nombre']])

print('')
arbol_nombre.inorden()
arbol_numero.inorden()
arbol_tipo.inorden() 

#b. 
print('DATOS DE UN POKEMON A PARTIR DE SU NUMERO Y NOMBRE: ')
arbol_numero.search_pokemon_por_numero(25)

arbol_nombre.search_pokemon_por_nombre("Mewtwo")

#c. 
print('POKEMON A PARTIR DE TIPO AGUA, FUEGO, PLANTA Y ELÉCTRICO: ')
arbol_tipo.inorden_tipos()

#d.
print('LISTADO ASCENDENTE POR NUMERO:')
arbol_numero.inorden_numero()
print('LISTADO ASCENDENTE POR NOMBRE:')
arbol_nombre.inorden_nombre()
print('LISTADO ASCENDENTE POR NIVEL POR NOMBRE:')
arbol_nombre.by_level_nombre()
#e.
print('INFO DE JOLTEON, LYCANROC Y TYRANTRUM:')
arbol_nombre.search_pokemon_por_nombre("Jolteon")
arbol_nombre.search_pokemon_por_nombre("Lycanroc")
arbol_nombre.search_pokemon_por_nombre("Tyrantrum")
#f.
contador_electricos=arbol_tipo.contador_pokemon_electricos()
print(f'CANTIDAD DE POKEMONES ELÉCTRICOS:{contador_electricos} ')
contador_acero= arbol_tipo.contador_pokemon_acero()
print(f'CANTIDAD DE POKEMONES ACERO:{contador_acero}')