import pygame
import sys
from constantes import *
from musica import *
from auxillar import Auxillar


def draw_text(text, font, color, x, y, screen):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


class button():
    def __init__(self, x, y, image, scale) -> None:
        ancho = image.get_width()
        alto = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(ancho*scale), int(alto*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False
        #
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
