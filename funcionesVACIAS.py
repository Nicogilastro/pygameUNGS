# -*- coding: utf-8 -*-
from principal import *
from configuracion import *
import random
import time

# Elije una palabra al azar de una lista

def nuevaPalabra(lista):
    largoLista = len(lista)
    numeroRandom = random.randint(0, largoLista - 1)
    return lista[numeroRandom]

# lee el archivo, y elije las letras que sean del largo especificado

def lectura(archivo, salida, largo):
    for palabra in archivo :
        if len(palabra) == largo:
            salida.append(palabra[:-1])

# chequea si la palabra ingresada por el usuario es correcta o no lo es, y las carga respectivamente a sus listas

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if len(palabra) > len(palabraCorrecta):
        palabra = ''
    for i in range(len(palabra)):
        if palabra[i].lower() == palabraCorrecta[i].lower() and palabra[i].lower() not in correctas:
            correctas.append(palabra[i])
            ding()
        elif palabra[i].lower() in palabraCorrecta and palabra[i].lower() not in casi and palabra[i].lower() not in correctas:
            casi.append(palabra[i])
            dung()
        elif palabra[i].lower() not in palabraCorrecta and palabra[i].lower() not in incorrectas:
            incorrectas.append(palabra[i])
            dong()
    
    if palabra == palabraCorrecta:
        return True
    else:
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

# sonidos

def ding():
    ding = pygame.mixer.Sound('./sonidos/ding.mp3')
    ding.set_volume(0.6)    
    ding.play(0)

def dong():
    dong = pygame.mixer.Sound('./sonidos/dong.mp3')
    dong.set_volume(0.6)    
    dong.play(0)

def dung():
    dung = pygame.mixer.Sound('./sonidos/dung.mp3')
    dung.set_volume(0.6)    
    dung.play(0)

# setea el juego para jugar por tiempo

# def porTiempo():
#     pass

# Muestra los primeros 10 mejores puntajes

# def records(nombre, cantAcertadas):
#     pass







