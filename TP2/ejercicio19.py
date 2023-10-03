from pila import Pila
# Transformers: la era de la extinción 	Paramount 2014
# El hobbit: la batalla de los Cinco Ejércitos 	Warner Bros 2014
# Vengadores: Infinity War 	Walt Disney Pictures/Marvel Studios 	2018
# Jurassic World: El reino caído 	Universal Pictures 2018
# Capitán América: Civil War marvel studio 2016
# Doctor Strange Marvel studio 2016


class Pelicula:
    def __init__(self, nombre, estudio, año):
        self.nombre = nombre
        self.estudio = estudio
        self.año = año


stack = Pila()
contador=0
# Cargando la pila

stack.push(Pelicula('Transofrmers', 'Paramount', 2014))
stack.push(Pelicula('El Hobbit: la batalla de los cinco ejercitos', 'Warner Bros', 2014))
stack.push(Pelicula('Vengadores: Infinity War','Walt Disney Pictures/Marvel Studios', 2018))
stack.push(Pelicula('Jurassic World: El reino caído','Universal Pictures', 2018))
stack.push(Pelicula('Capitan América: Civil war', 'Marvel Studio', 2016))
stack.push(Pelicula('Doctor Strange', 'Marvel Studio', 2016))

while stack.size()!=0:

    # if stack.on_top().estudio == 'Marvel Studio' and stack.on_top().año == 2016:
    #   print (f'La pelicula: {stack.on_top().nombre} es de Marvel, estrenada en 2016')
    
    if stack.on_top().año == 2014:
     
     print(f'La pelicula: {stack.on_top().nombre} se estrenó en 2014')

    if stack.on_top().año == 2018:
     contador+=1
    
    if stack.on_top().estudio == 'Marvel Studio' and stack.on_top().año == 2016:
      print(f'La pelicula: {stack.on_top().nombre} es de Marvel, estrenada en 2016')
     
    stack.pop()

print(f'La cantidad de peliculas estrenadas en 2018 son: {contador}')