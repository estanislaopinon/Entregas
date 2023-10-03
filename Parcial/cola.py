from random import randint


class Cola():

    def __init__(self):
        self.elementos = []

    def arrive(self, value):  # Agrega el elemento al final de la cola
        self.elementos.append(value)

    def atention(self):  # Elimina y devuelve el elemento almacenado en el frente de la cola
        if self.size() > 0:
            return self.elementos.pop(0)  # elimina el primero

    def size(self):  # devuelve la cantidad de elementos en la cola
        return len(self.elementos)

    def on_front(self):  # Devuelve el valor del elemento que esta almacenado en el frente de la cola sin eliminarlo
        if self.size() > 0:
            return self.elementos[0]

    # elimina el elemento en el frente de la cola y lo inserta en el final de la misma
    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux


# cola = Cola()
# # cola_aux = Cola()

# for i in range(5):
#     value = randint(1, 50)
#     cola.arrive(value)

# print()
# print(cola.atention())
# print(cola.atention())
# print(cola.on_front())
# print(cola.elementos)
# print(cola.size())

# while cola.size()>0:
#     value = cola.atention()
#     print(value)
#     cola_aux.arrive(value)

# print(cola.size())
# print(cola_aux.elementos)
# print(cola.elementos)
# print()
# cont=0
# while cont< cola.size():
#     value = cola.move_to_end()
#     print(value)
#     cont+=1

# print(cola.elementos)
