import pygame
import sys
from mapa import Mapa  # Asumo que tienes una clase Mapa en un archivo llamado Mapa.py
from Jtext import JTextArea
from button import Boton
from Jlabel import JLabel
# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 630, 630
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laberinto de Pac-Man")

imagen = pygame.image.load("C:\\Users\\Usuario\\Documents\\estructura de datos\\proyecto_final\\Captura de pantalla 2023-12-07 234908.png")
imagen_rect = imagen.get_rect()


Jmapa=JTextArea(380,175,100,50)
JLabel1= JLabel(180,200,"cantidad de cerezas")

Jmapa2=JTextArea(380,275,100,50)
JLabel2= JLabel(180,300,"cantidad de fantasmas")

Jmapa3=JTextArea(380,375,100,50)
JLabel3= JLabel(180,400,"cantidad de pastas")

boton=Boton(230,500,75,50,"Mapa 1")
boton2=Boton(330,500,75,50,"Mapa 2")
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
    screen.blit(imagen, imagen_rect)
    boton.draw(screen,(200,50,20),(250,250,250))
    Jmapa.draw(screen)
    JLabel1.draw(screen)
    boton2.draw(screen,(200,50,20),(250,250,250))
    Jmapa2.draw(screen)
    JLabel2.draw(screen)
    
    Jmapa3.draw(screen)
    JLabel3.draw(screen)
    # Dibujar el mapa
    if bandera:
        mi_mapa.draw()
    
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)


