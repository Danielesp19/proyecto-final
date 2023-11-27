import pygame
import sys
from mapa import Mapa  # Asumo que tienes una clase Mapa en un archivo llamado Mapa.py
from Jtext import JTextArea
from button import Boton
# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 730, 730
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laberinto de Pac-Man")
Jmapa=JTextArea(100,100,100,50)
boton=Boton(200,200,50,50,"GO")
# Crear un objeto Mapa
mi_mapa = Mapa()
bandera=False

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton.rect.collidepoint(event.pos):
                mi_mapa.selec_mapa(1, 4, 5, 2)  # Tipo 1, 3 fantasmas, 5 cerezas, 2 pastas
                bandera=True

    # Limpiar pantalla
    screen.fill((0, 0, 0))
    boton.draw(screen,(0,50,200),(0,0,0))
    Jmapa.draw(screen)
    
    # Dibujar el mapa
    if bandera:
        mi_mapa.draw()
    
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)

