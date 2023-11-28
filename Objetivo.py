import random
import pygame
class ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        
        if random.randint(1,2)==1:
            self.image = pygame.image.load("C:/Users/Usuario/Desktop/Captura de pantalla 2023-11-27 181743.png")
        else:
            self.image = pygame.image.load("C:/Users/Usuario/Desktop/Captura de pantalla 2023-11-27 183301.png")
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x+2
        self.rect.y = y+2

    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Cereza(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Usuario/Desktop/Captura de pantalla 2023-11-27 173922.png")
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-5

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Pastilla:
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Usuario/Downloads/1f48a-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-2

    def draw(self, surface):
        surface.blit(self.image, self.rect)


