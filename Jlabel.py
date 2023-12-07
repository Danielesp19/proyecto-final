import pygame
import sys

class JLabel:
    def __init__(self, x, y, text, font_size=22, text_color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.text_color = text_color

    def draw(self, surface):
        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(topleft=(self.x, self.y))
        surface.blit(text_surface, text_rect)

    def set_color(self, new_color):
        self.text_colorcolor = new_color