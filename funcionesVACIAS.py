# -*- coding: utf-8 -*-
from principal import *
from configuracion import *
import random

# Elije una palabra al azar de una lista

def nuevaPalabra(lista):
    largoLista = len(lista)
    numeroRandom = random.randint(0, largoLista - 1)
    return lista[numeroRandom]

# lee el archivo, y elije las letras que sean del largo especificado

def lectura(archivo, salida, largo):
    for palabra in archivo :
        if len(palabra) == largo:
            salida.append(palabra[:-1].lower())

# chequea si la palabra ingresada por el usuario es correcta o no lo es, y las carga respectivamente a sus listas

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if len(palabra) > len(palabraCorrecta):
        palabra = ''
    if palabra == palabraCorrecta:
        return True

    for i in range(len(palabra)):
        if palabra[i] == palabraCorrecta[i] and palabra[i] not in correctas:
            correctas.append(palabra[i])
            ding()
        elif palabra[i] in palabraCorrecta and palabra[i] not in casi and palabra[i] not in correctas:
            casi.append(palabra[i])
            dung()
        elif palabra[i] not in palabraCorrecta and palabra[i] not in incorrectas:
            incorrectas.append(palabra[i])
            dong()
    return False    

# sonidos

# sonido de acierto

def ding():
    ding = pygame.mixer.Sound('./sonidos/ding.mp3')
    ding.set_volume(0.6)    
    ding.play(0)

# sonido de acierto no certero

def dong():
    dong = pygame.mixer.Sound('./sonidos/dong.mp3')
    dong.set_volume(0.6)    
    dong.play(0)

# sonido de no acierto

def dung():
    dung = pygame.mixer.Sound('./sonidos/dung.mp3')
    dung.set_volume(0.6)    
    dung.play(0)
    