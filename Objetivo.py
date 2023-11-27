import pygame
class ghost:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = (0, 200, 0)
        print('se creo')

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
