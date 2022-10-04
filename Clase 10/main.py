#from re import I
import pygame
import random


# Inicializamos la libreria
pygame.init()


# Creamos tamaño de pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('./images/cohete.png')
pygame.display.set_icon(icono)

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
movimiento_enemigo_x = 0.3
movimiento_enemigo_y = 50

# Funcion jugador y variables
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion enemigo y variables
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Loop del juego - Creamos eventos
se_ejecuta = True
while se_ejecuta:

    # RGB Fondo
    pantalla.fill((205, 144, 228))
    
    # Iterar eventos
    for evento in pygame.event.get():
        
        # Evento Cerrar Programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        # Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            
            if evento.key == pygame.K_LEFT:
                
                movimiento_jugador_x = -0.1
            if evento.key == pygame.K_RIGHT:
                
                movimiento_jugador_x = 0.1
            

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
        movimiento_enemigo_x = 0.3
        enemigo_y += movimiento_enemigo_y
    elif enemigo_x >= 736:
        movimiento_enemigo_x = -0.3
        enemigo_y += movimiento_enemigo_y

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    pygame.display.update()