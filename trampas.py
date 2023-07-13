import pygame
from constantes import *
from auxillar import Auxillar


class trampas:
    def __init__(self, x, y) -> None:
        self.trampa = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Trampas\shuriken\shuriken_01.png", 8, 1)

        self.frame = 0
        self.animation = self.trampa
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.colision_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        self.tiempo_transcurrido_animation = 0

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if (self.tiempo_transcurrido_animation >= 70):
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


class fuego:
    def __init__(self, x, y) -> None:
        self.fuego = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Trampas\Fire.png", 4, 1)

        self.frame = 0
        self.animation = self.fuego
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.colision_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        self.tiempo_transcurrido_animation = 0

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if (self.tiempo_transcurrido_animation >= 70):
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
