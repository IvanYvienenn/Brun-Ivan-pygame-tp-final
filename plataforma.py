import pygame
from constantes import *
from auxillar import Auxillar


class plataforma:
    def __init__(self, x, y, ancho, alto, tipo) -> None:
        self.image = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos/Background/Assets/bloques.png", 4, 4)[tipo]
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_colision = pygame.Rect(
            self.rect.x, self.rect.y - 50 + self.rect.height, self.rect.width, 5)
        self.rect_bottom_colision = pygame.Rect(
            self.rect.x, self.rect.y + self.rect.height, self.rect.width, 5)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.rect)
            pygame.draw.rect(screen, VERDE, self.rect_ground_colision)
            pygame.draw.rect(screen, AZUL, self.rect_bottom_colision)


class plataforma_2:
    def __init__(self, x, y, ancho, alto, tipo) -> None:
        self.image = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos/Background/Assets/tiles.png", 2, 1)[tipo]
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_colision = pygame.Rect(
            self.rect.x, self.rect.y - 80 + self.rect.height, self.rect.width/2, 5)
        self.rect_bottom_colision = pygame.Rect(
            self.rect.x, self.rect.y + self.rect.height, self.rect.width, 5)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.rect)
            pygame.draw.rect(screen, VERDE, self.rect_ground_colision)
            pygame.draw.rect(screen, AZUL, self.rect_bottom_colision)
