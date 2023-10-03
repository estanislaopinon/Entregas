from random import randint
# #designar valor al sable_de_luz 

sable_de_luz=10


mochila =[]


for i in range(1,15):
    mochila.append(randint(0,15))


def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    if indice >= len(mochila):
        # Se llegó al final de la mochila sin encontrar un sable de luz
        print("No se encontró un sable de luz en la mochila.")
        return objetos_sacados
    elif mochila[indice] == sable_de_luz:
        # Se encontró un sable de luz
        objetos_sacados += 1
        print(f"Se encontró un sable de luz en la posición {indice+1} de la mochila.")
        print(f"Se sacaron {objetos_sacados-1} objetos de la mochila para encontrar el sable de luz.")
        return objetos_sacados
    else:
        # El objeto actual no es un sable de luz, continuar buscando
        objetos_sacados += 1
        return usar_la_fuerza(mochila, indice + 1, objetos_sacados)

usar_la_fuerza(mochila)



