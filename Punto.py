import pygame

class PuntoAmarillo:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 28, 28)  # Ajusté el tamaño del rectángulo
        self.color = (255, 255, 0)

    def draw(self, surface):
        # Dibuja el cuadrado
        pygame.draw.rect(surface, (0,0,0), self.rect)
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 5)