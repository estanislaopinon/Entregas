# 3. Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
# cual se almacenaban en una pila en cada misión de caza que
# emprendió(con la siguiente información planeta visitado, a quien
#           capturado, costo de la recompensa), resolver las siguientes
# actividades:
# a. Mostrar los planetas visitados en el orden hizo las misiones.
# b. Determinar cuántos créditos galácticos recaudo en total.
# c. Determinar el número de la misión en que capturo a Han Solo
# y en que planeta fue, suponga que dicha misión está cargada.
from pila import Pila
pila = Pila()
pila_aux = Pila()


class Registros():
    def __init__(self, planeta, captura, costo):
        self.planeta = planeta
        self.captura = captura
        self.costo = costo

    def __str__(self):
        return f"{self.planeta} - {self.captura} - {self.costo}"


def carga():
    pila.push(Registros("Tatooine", "Han Solo", 100000))
    pila.push(Registros("Coruscant", "Greedo", 50000))
    pila.push(Registros("Endor", "Wicket W. Warrick", 25000))
    pila.push(Registros("Hoth", "General Veers", 75000))
    pila.push(Registros("Bespin", "Lando Calrissian", 1500))

# a. Mostrar los planetas visitados en el orden hizo las misiones.


def misiones(pila):
    while pila.size() > 0:
        cosa = pila.pop()
        pila_aux.push(cosa)

    for j in range(pila_aux.size()):
        print(pila_aux.on_top())
        pila.push(pila_aux.on_top())
        pila_aux.pop()

# b. Determinar cuántos créditos galácticos recaudo en total.


def total(pila):
    resultado = 0
    while pila.size() > 0:

        resultado += pila.on_top().costo
        cosa = pila.pop()
        pila_aux.push(cosa)
    return resultado


carga()
# a. Mostrar los planetas visitados en el orden hizo las misiones.
misiones(pila)

i = total(pila)
print(i)
