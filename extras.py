# -*- coding: utf-8 -*-
import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *
    
def dameLetraApretada(key):
    if key == K_a:
        return ("a")
    elif key == K_b:
        return ("b")
    elif key == K_c:
        return ("c")
    elif key == K_d:
        return ("d")
    elif key == K_e:
        return ("e")
    elif key == K_f:
        return ("f")
    elif key == K_g:
        return ("g")
    elif key == K_h:
        return ("h")
    elif key == K_i:
        return ("i")
    elif key == K_j:
        return ("j")
    elif key == K_k:
        return ("k")
    elif key == K_l:
        return ("l")
    elif key == K_m:
        return ("m")
    elif key == K_n:
        return ("n")
    elif key == 59 or key == 241:
        return ("ñ")
    elif key == K_o:
        return ("o")
    elif key == K_p:
        return ("p")
    elif key == K_q:
        return ("q")
    elif key == K_r:
        return ("r")
    elif key == K_s:
        return ("s")
    elif key == K_t:
        return ("t")
    elif key == K_u:
        return ("u")
    elif key == K_v:
        return ("v")
    elif key == K_w:
        return ("w")
    elif key == K_x:
        return ("x")
    elif key == K_y:
        return ("y")
    elif key == K_z:
        return ("z")
    elif key == K_SLASH:
        return ("-")
    elif key == K_KP_MINUS:
        return ("-")
    elif key == K_SPACE:
       return (" ")
    else:
        return ("")

pygame.init()

defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    
defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

screen = pygame.display.set_mode((ANCHO, ALTO))

def colorIntentos(lista, palabraCorrecta, incorrectas):
    pos = 0
    for palabra in lista:
        posX = 0
        for i in range(len(palabra)):
            if palabra[i] == palabraCorrecta[i]:
                color = COLOR_LETRAS                
                screen.blit(defaultFontGrande.render(palabra[i], 1, color),((ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//2) + posX, 30 + 80 * pos))
            elif palabra[i] in palabraCorrecta:
                color = COLOR_AZUL
                screen.blit(defaultFontGrande.render(palabra[i], 1, color),((ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//2) + posX, 30 + 80 * pos))
            elif palabra[i] in incorrectas:
                color = COLOR_RED
                screen.blit(defaultFontGrande.render(palabra[i], 1, color),((ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//2) + posX, 30 + 80 * pos))
            posX += TAMANNO_LETRA_GRANDE
        pos += 1

# botones para la pantalla de reinicio

def botones():
    pygame.draw.rect(screen, COLOR_AZUL, [400, 400, 180 , 30])
    pygame.draw.rect(screen, COLOR_AZUL, [280, 400, 85 , 30])
    text = defaultFont.render('Jugar otra vez! (j)' , True , COLOR_BLANCO)
    text2 = defaultFont.render('Salir (s)' , True , COLOR_BLANCO)
    screen.blit(text , (405 , 405))
    screen.blit(text2 , (285 , 405))

# end screen when win

def ganaste(puntos, palabraCorrecta):
    screen = pygame.display.set_mode((ANCHO, ALTO))
    # pygame.mixer.music.stop()
    # mta = pygame.mixer.Sound('./sonidos/mta.mp3')
    # mta.set_volume(1)
    # mta.play(-1)
    text = defaultFont.render("Felicitaciones, tu puntaje es de " + str(puntos) + "!, La última palabra correcta era: " + palabraCorrecta, True, COLOR_VERDE)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])
    botones()
    
# end screen when loss

def perdiste(puntos, palabraCorrecta):
    screen = pygame.display.set_mode((ANCHO, ALTO))
    # pygame.mixer.music.stop()
    # loss = pygame.mixer.Sound('./sonidos/loss.mp3')
    # loss.set_volume(1)
    # loss.play()
    text = defaultFont.render("Perdiste, tu puntaje es de " + str(puntos) + "!, La palabra correcta era: " + palabraCorrecta, True, COLOR_RED)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])
    botones()

# revision del estado del juego, gano o perdio y sistema de records

def estadoDelJuego(puntos, palabraCorrecta, record):
    archivoPuntos=open("highscore.txt","r")
    record = archivoPuntos.readline()

    recordArchivo= int(record)

    archivoPuntos.close()
    archivoPuntos = open("highscore.txt", 'w')

    if puntos>recordArchivo:
        archivoPuntos.write(str(puntos))
        recordArchivo=puntos
        archivoPuntos.close()

    elif puntos < recordArchivo:
        archivoPuntos.write(record)
        archivoPuntos.close()

    else:
        archivoPuntos.write(str(puntos))

    if puntos == 0:
        perdiste(puntos, palabraCorrecta)
    else:
        ganaste(puntos, palabraCorrecta)
    archivoPuntos.close()
    

def dibujar(screen, listaDePalabrasUsuario, listaDiccionario, palabraUsuario, puntos, segundos, correctas, incorrectas, casi, intentos, palabraCorrecta, correctaAnterior):

    archivoPuntos = open("highscore.txt","r")
    RECORD = archivoPuntos.readline()
    archivoPuntos.close()

    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
        
    text = defaultFont.render("La última palabra correcta era: " + correctaAnterior, True, COLOR_VERDE)
    text_x = 400
    text_y = 500
    screen.blit(text, [text_x, text_y])

    # color de las letras despues de intetar
    
    colorIntentos(listaDePalabrasUsuario, palabraCorrecta, incorrectas)

    #Linea Horizontal
    pygame.draw.line(screen, (255, 255, 255), (0, ALTO-70), (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    if len(palabraUsuario) != LARGO - 1 :
        screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_RED), (190, 570))
        # muestra un mensaje para indicar que la palabra no tiene el largo correcto
        screen.blit(defaultFont.render("La palabra debe tener " + str(LARGO-1) + ' caracteres.', 1, COLOR_RED), (400, 570))
    else:
        screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_VERDE), (190, 570))
    #muestra el puntaje

    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))

    #muestra puntaje mas alto obtenido

    screen.blit(defaultFont.render("Record: " + str(RECORD), 1, COLOR_TEXTO), (680, 30))    

    #muestra los intentos

    screen.blit(defaultFont.render("Intentos: " + str(intentos), 1, COLOR_TEXTO), (680, 50))

    #muestra el largo de la palabra

    screen.blit(defaultFont.render("Largo de la Palabra: " + str(LARGO - 1), 1, COLOR_TEXTO), (300, 10))

    #muestra los segundos y puede cambiar de color con el tiempo

    if segundos < 15 :
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
        screen.blit(ren, (10, 10))
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
        screen.blit(ren, (10, 10))

    #muestra las palabras anteriores, las que se fueron arriesgando

    colorIntentos(listaDePalabrasUsuario, palabraCorrecta, incorrectas)

    # muestra un mensaje para indicar que la palabra no se puede repetir

    for palabra in listaDePalabrasUsuario:
        if palabraUsuario == palabra:
            screen.blit(defaultFont.render("La palabra no se puede repetir.", 1, COLOR_RED), (400, 550))

    # muestra un mensaje para indicar que la palabra debe estar en el diccionario

    if palabraUsuario not in listaDiccionario:
        screen.blit(defaultFont.render("La palabra debe estar en el diccionario.", 1, COLOR_RED), (400, 550))
    #muestra el abcdario, falta ponerle color a las letras
    abcdario = ["qwertyuiop", "asdfghjklñ", "zxcvbnm"]
    y = 0

    for abc in abcdario:
        x = 0
        for letra in abc:
            color = COLOR_TEXTO
            screen.blit(defaultFont.render(letra, 1, color),(10 + x, ALTO/1.5 + y))
            if letra in correctas:
                color = COLOR_LETRAS
                screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            elif letra in incorrectas:
                color = COLOR_RED
                screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            elif letra in casi:
                color = COLOR_AZUL
                screen.blit(defaultFont.render(letra, 1, color),(10 + x, ALTO/1.5 + y))

            x += TAMANNO_LETRA
        y += TAMANNO_LETRA

    if segundos < 0.01 or intentos == 0:
        estadoDelJuego(puntos, palabraCorrecta, RECORD) 
   