import pygame
from constantes import *
from auxillar import Auxillar
from musica import *


class platform:
    def __init__(self, x, y, w, h) -> None:
        self.platform = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos/Background/Assets/FallingPlatfrom.png", 8, 1)
        self.frame = 0
        self.contador = 0
        self.animation = self.platform
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.movement = 4
        self.colision_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.rect_ground_colision = pygame.Rect(
            self.rect.x, self.rect.y - 30 + self.rect.height, self.rect.width, 5)
        self.rect_bottom_colision = pygame.Rect(0, 0, 0, 0)

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= 30:
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.animation[self.frame]

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.colision_rect.y += delta_y
        self.rect_ground_colision.y += delta_y

    def do_move(self, delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if (self.tiempo_transcurrido_move >= 40):
            self.tiempo_transcurrido_move = 0
            self.change_y(self.move_y)
            if self.contador <= 50:
                self.move_y = -self.movement
                self.contador += 1

            elif self.contador <= 100:
                self.move_y = self.movement
                self.contador += 1

            else:
                self.contador = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.rect)
            pygame.draw.rect(screen, AZUL, self.colision_rect)
            pygame.draw.rect(screen, VERDE, self.rect_ground_colision)
