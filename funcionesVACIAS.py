from principal import *
from configuracion import *
import random
import math

# Elije una palabra al azar de una lista

def nuevaPalabra(lista):
    largoLista = len(lista)
    numeroRandom = random.randint(0, largoLista)
    print(lista[numeroRandom])
    return lista[numeroRandom]

# lee el archivo, y elije las letras que sean del largo especificado

def lectura(archivo, salida, largo):
    for palabra in archivo :
        if len(palabra) == largo:
            salida.append(palabra)
    return salida

# chequea si la palabra ingresada por el usuario es correcta o no lo es, y las carga respectivamente a sus listas

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if palabraCorrecta == palabra :
        correctas.append(palabra)
        return True
    else :
        incorrectas.append(palabra)
        for letra in palabra:
            if letra in palabraCorrecta:
                casi.append(letra)
        return False


# chequea la longitud de la palabra ingresada si es igual al de la palabra oculta

def longitudPalabra(palabra, largo):
    if len(palabra) == largo :
        return True
    else :
        return False

# checkea si la letra esta en la lista de "casi"

def letraEnCasi(letra, casi):
    if letra in casi:
        return True
    else:
        return False

# setea el juego para jugar por tiempo

def porTiempo():
    return

# Indica si el jugador gano o perdio, mostrando la palabra correcta

def cierre():
    return

# Muestra los primeros 10 mejores puntajes

def records(nombre, cantAcertadas):
    return







