import pygame
import sys

class Pared:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = (30, 30, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)