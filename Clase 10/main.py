#from re import I
import pygame
import random
import math
from pygame import mixer


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

# Agregar musica
mixer.music.load('./media/MusicaFondo.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)


#Creamos jugador
img_jugador = pygame.image.load('./images/nave.png')

#Ubicacion inicial
jugador_x = 368 #centro eje x = ancho pantalla/2 - mitad de img_jugador (800/2 - 64/2)
jugador_y = 536 # Base de Y = tamaño de y - img_jugador/2
movimiento_jugador_x = 0

#Creamos enemigos (Probar hacerlo con clases)

img_enemigo = []
enemigo_x = []
enemigo_y = []
movimiento_enemigo_x = []
movimiento_enemigo_y = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('./images/enemigo.png'))
    enemigo_x.append(random.randint(0,736)) #centro eje x = ancho pantalla/2 - mitad de img_enemigo (800/2 - 64/2)
    enemigo_y.append(random.randint(50,200)) # Base de Y = tamaño de y - img_enemigo/2
    movimiento_enemigo_x.append(0.5)
    movimiento_enemigo_y.append(50)


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
fuente = pygame.font.Font('./fonts/GemunuLibre-Regular.ttf', 32)
texto_x = 10
texto_y = 10

# texto final del juego
fuente_final = pygame.font.Font('./fonts/GemunuLibre-Regular.ttf', 60)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (200, 200))

# Funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion jugador y variables
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion enemigo y variables
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

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
                sonido_bala = mixer.Sound('./media/disparo.mp3')
                sonido_bala.play()
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
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 498:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000 #Valor exajerado para sacar al enemigo fuera de pantalla
            texto_final()
            break

        enemigo_x[e] += movimiento_enemigo_x[e]

        # mantener dentro del borde enemigo
        if enemigo_x[e] <= 0:
            movimiento_enemigo_x[e] = 0.5
            enemigo_y[e] += movimiento_enemigo_y[e]
        
        elif enemigo_x[e] >= 736:
            
            movimiento_enemigo_x[e] = -0.5
            enemigo_y[e] += movimiento_enemigo_y[e]

        # Colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)

        if colision:
            sonido_colision = mixer.Sound('./media/Golpe.mp3')
            sonido_colision.play()
            bala_y= 500
            bala_visible = False
            puntaje +=1
            enemigo_x[e] = random.randint(0,736) #centro eje x = ancho pantalla/2 - mitad de img_enemigo (800/2 - 64/2)
            enemigo_y[e] = random.randint(50,200) # Base de Y = tamaño de y - img_enemigo/2

        enemigo(enemigo_x[e], enemigo_y[e], e)


    # Movimiento Bala
    if bala_y <= -64:    #Tamaño bala
        
        bala_visible = False
        bala_y = 500
    
    if bala_visible:

        disparar_bala(bala_x, bala_y)
        bala_y -= movimiento_bala_y

    
    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)
    
    # Referescamos pantalla
    pygame.display.update()