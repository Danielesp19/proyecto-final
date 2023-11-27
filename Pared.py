import pygame
import sys

class pared:
    
    def __init__(self,x,y,ancho,alto):
        self.rect=pygame.rect(x,y,ancho,alto)
        self.background_color=(0,0,0)
        

    def draw(self,surface):
        pygame.draw.rect( surface, self.rect, self.background_color)