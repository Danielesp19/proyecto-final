import pygame
import sys

class Pared:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = (0, 0, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class ghost:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = (0, 200, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class PuntoAmarillo:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x+10, y+10, 8, 8)
        self.color = (255, 255, 0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 2)

class Mapa:
    def __init__(self):
        self.vec_paredes = []

    def cargar_mapa(self, mapa):
        for row_index, row in enumerate(mapa):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    pared = Pared(col_index * 30, row_index * 30, 30, 30)
                    self.vec_paredes.append(pared)
                if cell == 3:
                    ghosts = ghost(col_index * 30, row_index * 30, 30, 30)
                    self.vec_paredes.append(ghosts)
                if cell==0:
                    Punto=PuntoAmarillo(col_index * 30, row_index * 30)
                    self.vec_paredes.append(Punto)



    def draw(self, surface):
        for pared in self.vec_paredes:
            pared.draw(surface)

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 630, 630
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laberinto de Pac-Man")

# Crear un mapa y agregar paredes
mi_mapa = Mapa()

# Definir el laberinto (1 representa una pared, 0 representa espacio vacío)
mapa_lab = [
    #1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20   21
    [7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7], #1
    [7 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 7], #2
    [7 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 7], #3
    [7 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 7], #4
    [7 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 7], #5
    [7 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 7], #6
    [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #7
    [7 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 7], #8
    [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #9
    [7 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 7], #10
    [7 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 7], #11
    [7 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 7], #12
    [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #13 
    [7 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 7], #14
    [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #15
    [7 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 7], #16
    [7 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 7], #17
    [7 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 7], #18
    [7 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 7], #19
    [7 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 7], #20
    [7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7], #21
]

if mapa_lab[10][10]==0:
    mapa_lab[10][10]=3

mi_mapa.cargar_mapa(mapa_lab)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Dibujar el mapa
    mi_mapa.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)