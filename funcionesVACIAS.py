# -*- coding: utf-8 -*-
from principal import *
from configuracion import *
import random
import time

# Elije una palabra al azar de una lista

def nuevaPalabra(lista):
    largoLista = len(lista)
    numeroRandom = random.randint(0, largoLista)
    # print(lista[numeroRandom])
    return lista[numeroRandom]

# lee el archivo, y elije las letras que sean del largo especificado

def lectura(archivo, salida, largo):
    for palabra in archivo :
        if len(palabra) == largo:
            salida.append(palabra[:-1])

# largo de la palabra usuario

def largoPalabra():
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    screen = pygame.display.set_mode((ANCHO, ALTO))
    text = defaultFont.render("La palabra no puede tener mas de " + str(LARGO-1) + ' caracteres.', True, COLOR_AZUL)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])

# chequea si la palabra ingresada por el usuario es correcta o no lo es, y las carga respectivamente a sus listas

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if len(palabra) > len(palabraCorrecta):
        palabra = ''
        
    for i in range(len(palabra)):
        if palabra[i] == palabraCorrecta[i] and palabra[i] not in correctas:
            correctas.append(palabra[i])
        elif palabra[i] in palabraCorrecta and palabra[i] not in casi and palabra[i] not in correctas:
            casi.append(palabra[i])
        elif palabra[i] not in palabraCorrecta and palabra[i] not in incorrectas:
            incorrectas.append(palabra[i])
    if palabra == palabraCorrecta:
        return True        

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
    ding = pygame.mixer.Sound('./pygameUNGS/sonidos/ding.mp3')
    ding.set_volume(0.6)    
    ding.play(0)
    # pygame.time.wait(int(ding.get_length() * 1000))
    
def dingNO():
    ding = pygame.mixer.Sound('./pygameUNGS/sonidos/ding.mp3')
    ding.set_volume(0)    
    ding.stop()
    # pygame.time.wait(int(ding.get_length() * 1000))

def dong():
    dong = pygame.mixer.Sound('./pygameUNGS/sonidos/dong.mp3')
    dong.set_volume(0.6)    
    dong.play(0)
    # pygame.time.wait(int(dong.get_length() * 1000))

def dung():
    dung = pygame.mixer.Sound('./pygameUNGS/sonidos/dung.mp3')
    dung.set_volume(0.6)    
    dung.play(0)
    # pygame.time.wait(int(dung.get_length() * 1000))

# setea el juego para jugar por tiempo

def porTiempo():
    return

# Muestra los primeros 10 mejores puntajes

def records(nombre, cantAcertadas):
    return







