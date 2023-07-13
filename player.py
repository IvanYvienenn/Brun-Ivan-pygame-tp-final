import pygame
from constantes import *
from auxillar import *
from musica import *
from enemigo import Skeleton_enemy,Boss
from botin import coins, Health_up
from trampas import trampas
from plataforma_dinamica import platform


class Player_1():
    def __init__(self, x, y, gravity, jump_power, jump_height) -> None:
        self.walk_r = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Walk.png", 8, 1)
        self.walk_l = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Walk.png", 8, 1, True)
        self.idle_r = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Idle.png", 14, 1)
        self.idle_l = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Idle.png", 14, 1, True)
        self.jump_r = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Jump.png", 19, 1)
        self.jump_l = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Jump.png", 19, 1, True)
        self.attack_r = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Attack.png", 7, 1)
        self.attack_l = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Knight\Kinight_Sheet\Attack.png", 7, 1, True)
        self.frame = 0
        self.lives = 1000
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.y_start_jump = 0
        self.jump = jump_power
        self.jump_height = jump_height
        self.speed = 5
        self.gravity = gravity
        self.is_jump = False
        self.is_attack = False
        self.is_falling = False
        self.direction = DIRECTION_L

        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0
        self.interval_time_jump = 100

        self.animation = self.idle_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.colision_rect = pygame.Rect(
            x, y, self.rect.width / 3, self.rect.height / 3)
        self.colision_rect.center = self.rect.center
        self.ground_colision_rect = pygame.Rect(self.colision_rect)
        self.ground_colision_rect.height = 8
        self.ground_colision_rect.y = y + self.rect.height - 37

    def Walk(self, direction):
        if (self.is_jump == False):
            if (self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if (direction == DIRECTION_R):
                    self.move_x = self.speed
                    self.animation = self.walk_r

                else:
                    self.move_x = -self.speed
                    self.animation = self.walk_l

    def attack(self, on_off=True):
        self.is_attack = on_off
        if (on_off == True and self.is_jump == False and self.is_falling == False):
            if (self.animation != self.attack_r and self.animation != self.attack_l):
                self.frame = 0
                if (self.direction == DIRECTION_R):
                    self.animation = self.attack_r
                else:
                    self.animation = self.attack_l
                self.move_x = 0

    def Jump(self, on_off=True):
        if on_off and self.is_jump == False and self.is_falling == False:
            self.y_start_jump = self.rect.y
            if (self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 1.2)
                self.move_y = -self.jump
                self.animation = self.jump_r
            else:
                self.move_y = -self.jump
                self.move_x = int(self.move_x / 1.2)
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
            if (jump_sound.get_num_channels() == 0):
                jump_sound.play()
        if (on_off == False):
            self.is_jump = False
            self.Idle()

    def Idle(self):
        if (self.is_attack == True):
            return

        if (self.animation != self.idle_r and self.animation != self.idle_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.idle_r
            else:
                self.animation = self.idle_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_move(self, delta_ms, lista_plataformas, lista_plataformas_dinamicas):
        self.tiempo_transcurrido_move += delta_ms
        if (self.tiempo_transcurrido_move >= 10):
            if (abs(self.y_start_jump) - abs(self.rect.y) >= self.jump_height and self.is_jump):
                self.move_y = 0
            self.tiempo_transcurrido_move = 0
            self.mover_x(self.move_x)
            self.mover_y(self.move_y)
        if (self.colision_rect.right >= ANCHO_VENTANA or self.colision_rect.left <= 0):
            self.mover_x(-self.move_x)
        if (self.colision_rect.top <= 0):
            self.move_y = 0

        if (self.is_on_platform(lista_plataformas) == False) and (self.is_on_platform(lista_plataformas_dinamicas) == False):
            if (self.move_y == 0):
                self.is_falling = True
                self.mover_y(self.gravity)
        else:
            if (self.is_jump):
                self.is_jump = False
            self.is_falling = False

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if (self.tiempo_transcurrido_animation >= 50):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0

    def is_on_platform(self, lista_plataformas):
        retorno = False
        if (self.rect.y >= 800):
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if (self.ground_colision_rect.colliderect(plataforma.rect_ground_colision)):
                    if (self.is_falling == True and fall_sound.get_num_channels() == 0):
                        fall_sound.play()
                    retorno = True

                    break
                elif (self.colision_rect.colliderect(plataforma.rect_bottom_colision)):
                    self.move_y = 0
                    break
        return retorno

    def mover_x(self, delta_x):
        self.rect.x += delta_x
        self.colision_rect.x += delta_x
        self.ground_colision_rect.x += delta_x

    def mover_y(self, delta_y):
        self.rect.y += delta_y
        self.colision_rect.y += delta_y
        self.ground_colision_rect.y += delta_y

    def update(self, delta_ms, lista_plataformas, lista_plataformas_dinamicas):
        self.do_move(delta_ms, lista_plataformas, lista_plataformas_dinamicas)
        self.do_animation(delta_ms)

    def draw(self, screen):
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.colision_rect)
            pygame.draw.rect(screen, VERDE, self.ground_colision_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

    def events(self, keys, delta_ms):
        self.tiempo_transcurrido += delta_ms

        if (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_j]):
            self.Walk(DIRECTION_L)

        if (not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_j]):
            self.Walk(DIRECTION_R)

        if (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_UP]) and not keys[pygame.K_j]:
            self.Idle()
        if (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_UP]):
            self.Idle()

        if (keys[pygame.K_UP] and not keys[pygame.K_j]):
            if ((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.Jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if (not keys[pygame.K_j]):
            self.attack(False)

        if (keys[pygame.K_j]):
            if (attack_sound.get_num_channels() == 0):
                attack_sound.play()
            self.attack()

    def knight_collide(self, lista_enemigos, lista_items, lista_trampas, lista_plataformas_dinamicas):
        for enemigo in lista_enemigos:
            if type(enemigo) == Skeleton_enemy:
                if(self.colision_rect.colliderect(enemigo.colision_rect) and self.is_attack == True):
                    self.score += 1
                if (self.colision_rect.colliderect(enemigo.colision_rect) and enemigo.is_attack == True):
                    self.lives -= 1
            if type(enemigo) == Boss:
                if (self.colision_rect.colliderect(enemigo.colision_rect) and self.is_attack == True):
                    self.score += 1
                if (self.colision_rect.colliderect(enemigo.colision_rect) and enemigo.is_attack == True):
                    self.lives -= 2
        for item in lista_items:
            if (self.colision_rect.colliderect(item.colision_rect)):
                if type(item) == coins:
                    coin_sound.play()
                    self.score += 50
                if type(item) == Health_up:
                    health_sound.play()
                    self.lives += 500
                item.rect.x = -10000
                item.colision_rect.x = -10000
        for trampa in lista_trampas:
            if (self.colision_rect.colliderect(trampa.colision_rect)):
                self.lives -= 1
        for plataforma in lista_plataformas_dinamicas:
            if (self.ground_colision_rect.colliderect(plataforma.rect_ground_colision)):
                self.move_y = 0
                self.mover_y(-self.gravity)
                self.is_falling = False
                self.is_jump = False
                self.is_on_platform(lista_plataformas_dinamicas)
                break
        if type(lista_plataformas_dinamicas) == True:
            if (self.is_on_platform(lista_plataformas_dinamicas) == False):
                if (self.move_y == 0):
                    self.is_falling = True
                    self.mover_y(self.gravity)
                else:
                    self.move_y = 0
            else:
                if (self.is_jump):
                    self.is_jump = False
                self.is_falling = False
