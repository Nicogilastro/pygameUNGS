#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import sys
import math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *

#Funcion principal

def main():
    #Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()

    #Preparar la ventana
    pygame.display.set_caption("La escondida...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0
    palabraUsuario = ""
    listaPalabrasDiccionario = []
    ListaDePalabrasUsuario = []
    correctas = []
    incorrectas = []
    casi = []
    gano = False
    correctaAnterior = ''

    archivo = open("./lemario.txt", "r")

    #lectura del diccionario

    lectura(archivo, listaPalabrasDiccionario, LARGO)

    #elige una al azar
    palabraCorrecta = nuevaPalabra(listaPalabrasDiccionario)

    # musica de fondo

    music = pygame.mixer.music.load('./sonidos/gta.mp3')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    intentos = 5

    dibujar(screen, ListaDePalabrasUsuario, listaPalabrasDiccionario, palabraUsuario, puntos, segundos, correctas, incorrectas, casi, intentos, palabraCorrecta, correctaAnterior)

    while segundos > fps/1000 and intentos > 0 and not gano:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                palabraUsuario += letra  # es la palabra que escribe el usuario
                if e.key == K_BACKSPACE:
                    palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                if e.key == K_RETURN:
                    if len(palabraUsuario) == (LARGO - 1) and palabraUsuario not in ListaDePalabrasUsuario:
                        if palabraUsuario in listaPalabrasDiccionario:
                            gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                            if palabraUsuario not in ListaDePalabrasUsuario:
                                ListaDePalabrasUsuario.append(palabraUsuario)
                            if gano:
                                puntos += 1
                                palabraUsuario = ""
                                ListaDePalabrasUsuario = []
                                correctas = []
                                incorrectas = []
                                casi = []
                                gano = False
                                intentos = 6
                                correctaAnterior = palabraCorrecta                                
                                palabraCorrecta = nuevaPalabra(listaPalabrasDiccionario)
                                dibujar(screen, ListaDePalabrasUsuario, listaPalabrasDiccionario, palabraUsuario, puntos, segundos, correctas, incorrectas, casi, intentos, palabraCorrecta, correctaAnterior)                                
                            palabraUsuario = ''
                            intentos -= 1

        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

        #Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        #Dibujar de nuevo todo
        dibujar(screen, ListaDePalabrasUsuario, listaPalabrasDiccionario, palabraUsuario, puntos, segundos, correctas, incorrectas, casi, intentos, palabraCorrecta, correctaAnterior)

        pygame.display.flip()

    def botonApretado():
        inputUsuario = ''
        pygame.init()
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                inputUsuario += letra
                if inputUsuario == "s":
                    pygame.display.quit()
                    exit()    
                elif inputUsuario == "j":
                    pygame.display.quit()
                    pygame.quit()
                    main()
            
    while 1:
        if segundos < 0.01 or intentos == 0:
            botonApretado()

    archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()