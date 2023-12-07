import pygame
import sys
from mapa import Mapa  # Asumo que tienes una clase Mapa en un archivo llamado Mapa.py
from Jtext import JTextArea
from button import Boton
from Jlabel import JLabel
# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 730, 730
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laberinto de Pac-Man")


Jmapa=JTextArea(400,175,100,50)
JLabel1= JLabel(200,200,"cantidad de cerezas")

Jmapa2=JTextArea(400,275,100,50)
JLabel2= JLabel(200,300,"cantidad de fantasmas")

Jmapa3=JTextArea(400,375,100,50)
JLabel3= JLabel(200,400,"cantidad de pastas")

boton=Boton(250,500,75,50,"Mapa 1")
boton2=Boton(350,500,75,50,"Mapa 2")
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
                mi_mapa.selec_mapa(1, Jmapa2.get_numeroS()[-1], Jmapa.get_numeroS()[-1], Jmapa3.get_numeroS()[-1])  # Tipo 1, 3 fantasmas, 5 cerezas, 2 pastas
                
                bandera=True
            if boton2.rect.collidepoint(event.pos):
                mi_mapa.selec_mapa(2, Jmapa2.get_numeroS()[-1], Jmapa.get_numeroS()[-1], Jmapa3.get_numeroS()[-1])
                
                bandera=True
        Jmapa2.handle_event(event)
        Jmapa.handle_event(event)
        Jmapa3.handle_event(event)
    # Limpiar pantalla
    screen.fill((0, 0, 0))
    boton.draw(screen,(0,50,200),(0,0,0))
    Jmapa.draw(screen)
    JLabel1.draw(screen)
    boton2.draw(screen,(0,50,200),(0,0,0))
    Jmapa2.draw(screen)
    JLabel2.draw(screen)
    
    Jmapa3.draw(screen)
    JLabel3.draw(screen)
    # Dibujar el mapa
    if bandera:
        mi_mapa.draw()
    
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)


