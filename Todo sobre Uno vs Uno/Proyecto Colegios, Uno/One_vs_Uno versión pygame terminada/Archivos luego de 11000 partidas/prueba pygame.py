from FuncionesIntocables import *
#### Modulos de Pygame #########
import pygame, sys, time
from pygame.locals import *
from Utilidades import *
screen = pygame.display.set_mode(DIMENSION)
pygame.display.set_caption("El One Vs Uno")

fondo_juego = pygame.image.load("img/"+"fondo2.jpg").convert()
if fondo_juego.get_size() != DIMENSION: 
    fondo_juego = pygame.transform.scale(fondo_juego, DIMENSION)

imagenes_cartas = dict()

for tuplacarta, archivo in IMAGENES_CARTAS.items():
    imagen = pygame.image.load("img/"+archivo).convert_alpha()

    if imagen.get_size() != (50, 100):
        imagen = pygame.transform.scale(imagen, (50, 100))
        
    imagenes_cartas[tuplacarta] = imagen
print imagenes_cartas
while True:
    a=raw_input("lel ")
    #screen.fill((0,0,0))
    #pygame.display.flip()
    #event = pygame.event.poll()
    #if event.type == pygame.QUIT:
        #running = 0
    #a=raw_input("lel")
    #screen.fill((100, 200, 0))
    #pygame.display.flip()
    
