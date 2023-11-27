import pygame
class PuntoAmarillo:
    def __init__(self, x, y):
        self.rect2= pygame.Rect(x, y, 30, 30)
        self.rect = pygame.Rect(x+10, y+10, 8, 8)
        self.color = (255, 255, 0)

    def draw(self, surface):
        pygame.draw.rect(surface,(0,0,0),self.rect2)
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 2)