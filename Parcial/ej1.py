# Desarrollar una función recursiva que permita contar cuantas veces
# aparece una determinada palabra, en un vector de palabras.

def contador_palabra(palabra, vector):

    if not vector:
        return 0
    elif vector[0] == palabra:
        return 1 + contador_palabra(palabra, vector[1:])
    else:
        return contador_palabra(palabra, vector[1:])


Palabras = ["perro", "gato", "llave", "gato", "perro", "perro", "tuerca"]
print(Palabras)
palabra_a_buscar = input("Ingrese la palabra a buscar: ")

contador = contador_palabra(palabra_a_buscar, Palabras)

print(f'La palabra {palabra_a_buscar} aparece {contador} veces')
