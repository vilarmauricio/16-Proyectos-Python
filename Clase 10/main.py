#from re import I
import pygame
import random
import math


# Inicializamos la libreria
pygame.init()


# Creamos tamaño de pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('./images/cohete.png')
pygame.display.set_icon(icono)

#Creamos imagen fondo
imagen_fondo = pygame.image.load('./images/Fondo.jpg')

#Creamos jugador
img_jugador = pygame.image.load('./images/nave.png')

#Ubicacion inicial
jugador_x = 368 #centro eje x = ancho pantalla/2 - mitad de img_jugador (800/2 - 64/2)
jugador_y = 536 # Base de Y = tamaño de y - img_jugador/2
movimiento_jugador_x = 0

#Creamos enemigo
img_enemigo = pygame.image.load('./images/enemigo.png')

#Ubicacion inicial enemigo
enemigo_x = random.randint(0,736) #centro eje x = ancho pantalla/2 - mitad de img_enemigo (800/2 - 64/2)
enemigo_y = random.randint(50,200) # Base de Y = tamaño de y - img_enemigo/2
movimiento_enemigo_x = 0.5
movimiento_enemigo_y = 50

#Creamos bala
img_bala = pygame.image.load('./images/bala.png')

#Ubicacion inicial bala
bala_x = 0
bala_y = 500
movimiento_bala_x = 0
movimiento_bala_y = 2
bala_visible = False

# Puntaje
puntaje = 0


# Funcion jugador y variables
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion enemigo y variables
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

#Funcion disparar Bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10)) # +16 y +10 centran la bala en la punta de la nave

# Funcion detectar Colision
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2)+ math.pow(y_2 - y_1,2))
    if distancia < 27: # Buscamos una distancia optima
        return True
    else:
        return False

# Loop del juego - Creamos eventos
se_ejecuta = True
while se_ejecuta:

    #Imagen Fondo
    pantalla.blit(imagen_fondo, (0,0))

    
    # RGB Fondo color solido
    #pantalla.fill((205, 144, 228))
    
    # Iterar eventos
    for evento in pygame.event.get():
        
        # Evento Cerrar Programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            
            if evento.key == pygame.K_LEFT:
                
                movimiento_jugador_x = -1
            if evento.key == pygame.K_RIGHT:
                
                movimiento_jugador_x = 1

            if evento.key == pygame.K_SPACE:
                if bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
            

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                movimiento_jugador_x = 0
    
    
    # Modificar ubicacion jugador
    jugador_x += movimiento_jugador_x

    # mantener dentro del borde enemigo
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    # Modificar ubicacion enemigo
    enemigo_x += movimiento_enemigo_x

    # mantener dentro del borde enemigo
    if enemigo_x <= 0:
        movimiento_enemigo_x = 0.5
        enemigo_y += movimiento_enemigo_y
    
    elif enemigo_x >= 736:
        
        movimiento_enemigo_x = -0.5
        enemigo_y += movimiento_enemigo_y

    # Movimiento Bala
    if bala_y <= -64:    #Tamaño bala
        
        bala_visible = False
        bala_y = 500
    
    if bala_visible:

        disparar_bala(bala_x, bala_y)
        bala_y -= movimiento_bala_y

    # Colision
    colision = hay_colision(enemigo_x, enemigo_y, bala_x, bala_y)

    if colision:
        bala_y= 500
        bala_visible = False
        puntaje +=1
        print(puntaje)
        enemigo_x = random.randint(0,736) #centro eje x = ancho pantalla/2 - mitad de img_enemigo (800/2 - 64/2)
        enemigo_y = random.randint(50,200) # Base de Y = tamaño de y - img_enemigo/2



    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    pygame.display.update()