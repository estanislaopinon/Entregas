from random import randint


class Cola():

    def __init__(self):
        self.elementos = []

    #agrega el elemento al final de la cola
    def arrive(self, value):
        self.elementos.append(value)

    #elimina y devuelve el elemento almacenado en el frente de la cola
    def atention(self):
        if self.size() > 0:
            return self.elementos.pop(0)  # elimina el primero
    
    def size(self):
        return len(self.elementos)

    #devuelve el valor del elemento que esta almacenado en el frente de la cola sin eliminarlo
    def on_front(self):
        if self.size() > 0:
            return self.elementos[0]

    #elimina el elemento en el frente de la cola y lo inserta en el final de la misma
    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux


cola = Cola()
# cola_aux = Cola()

for i in range(5):
    value = randint(1, 50)
    cola.arrive(value)
