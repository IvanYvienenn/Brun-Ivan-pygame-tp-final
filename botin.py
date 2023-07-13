import pygame
from constantes import *
from auxillar import Auxillar
from musica import *


class coins:
    def __init__(self, x, y) -> None:
        self.coin = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos/Items/MonedaD.png", 5, 1)
        self.frame = 0
        self.animation = self.coin
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.colision_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= 120:
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.animation[self.frame]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.rect)


class Health_up:
    def __init__(self, x, y) -> None:
        self.health_up = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos/Items/Health_up.png", 4, 1)
        self.frame = 0
        self.animation = self.health_up
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.colision_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= 120:
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.animation[self.frame]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.rect)
