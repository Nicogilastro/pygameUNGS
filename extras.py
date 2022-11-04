# from curses import COLOR_RED
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
    elif key == 59:
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

def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,
            correctas, incorrectas, casi, intentos, palabraCorrecta):
    defaultFont = pygame.font.Font(
        pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande = pygame.font.Font(
        pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    # botones para la pantalla de reinicio

    def botones():
        pygame.draw.rect(screen, COLOR_AZUL, [400, 400, 155 , 30])
        pygame.draw.rect(screen, COLOR_AZUL, [280, 400, 60 , 30])
        text = defaultFont.render('Jugar otra vez!' , True , COLOR_BLANCO)
        text2 = defaultFont.render('Salir' , True , COLOR_BLANCO)
        screen.blit(text , (405 , 405))
        screen.blit(text2 , (285 , 405))
        # get all events
        ev = pygame.event.get()

        # proceed events
        for event in ev:
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()

            # get a list of all sprites that are under the mouse cursor
            # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # do something with the clicked sprites...
    # end screen when win

    def ganaste():
        screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.mixer.music.stop()
        mta = pygame.mixer.Sound('./sonidos/mta.mp3')
        mta.set_volume(1)
        mta.play(-1)
        text = defaultFont.render("Ganaste!, la palabra correcta era: " + palabraCorrecta, True, COLOR_VERDE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        botones()
        
    # end screen when loss

    def perdiste():
        screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.mixer.music.stop()
        loss = pygame.mixer.Sound('./sonidos/loss.mp3')
        loss.set_volume(1)
        loss.play()
        text = defaultFont.render("Perdiste, la palabra correcta era: " + palabraCorrecta, True, COLOR_RED)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        botones()

    #Linea Horizontal
    pygame.draw.line(screen, (255, 255, 255), (0, ALTO-70), (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra el largo de la palabra
    screen.blit(defaultFont.render("Largo de la Palabra: " + str(LARGO - 1), 1, COLOR_TEXTO), (300, 10))
    #muestra los intentos
    screen.blit(defaultFont.render("Intentos: " + str(intentos), 1, COLOR_TEXTO), (680, 30))
    #muestra los segundos y puede cambiar de color con el tiempo

    if segundos < 15 :
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
        screen.blit(ren, (10, 10))
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
        screen.blit(ren, (10, 10))

    #muestra las palabras anteriores, las que se fueron arriesgando
    pos = 0
    for palabra in listaDePalabrasUsuario:
        screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS),(ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4, 30 + 80 * pos))
        pos += 1

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

    if gano:
        ganaste()
    else:
        if intentos == 0 and palabraUsuario != palabraCorrecta:
            perdiste()
        if segundos < 1:
            perdiste()

