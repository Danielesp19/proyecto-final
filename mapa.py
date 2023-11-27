import pygame
import sys

class mapa:
    
    def __init__(self,x,y,ancho,alto):
        self.rect=pygame.rect(x,y,ancho,alto)
        self.background_color=(0,0,0)
        self.vec_paredes=[]


    def draw(self,surface):
        pygame.draw.rect( surface, self.rect, self.background_color)
