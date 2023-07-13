import pygame
from constantes import *
from auxillar import Auxillar



class Skeleton_enemy:
    def __init__(self, x, y, gravity, speed,) -> None:
        self.walk_r = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Skeleton_enemy\Walk.png", 12, 1)
        self.walk_l = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Skeleton_enemy\Walk.png", 12, 1, True)
        self.attack_r = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Skeleton_enemy\Attack.png", 13, 1)
        self.attack_l = Auxillar.getSurfaceFromSpriteSheet(
            "Recursos\Skeleton_enemy\Attack.png", 13, 1, True)
        self.death_r = Auxillar.getSurfaceFromSpriteSheet("Recursos\Skeleton_enemy\death.png", 13, 1)
        self.death_l = Auxillar.getSurfaceFromSpriteSheet("Recursos\Skeleton_enemy\death.png", 13, 1, True)
        self.contador = 0
        self.frame = 0
        self.health = 50
        self.move_x = 0
        self.move_y = 0
        self.speed = speed
        self.gravity = gravity
        self.animation = self.walk_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_jump = False
        self.is_fall = False
        self.is_attack = False
        self.is_death = False

        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.colision_rect = pygame.Rect(
            x+self.rect.width/3, y, self.rect.width/3, self.rect.height)
        self.ground_colision_rect = pygame.Rect(self.colision_rect)
        self.ground_colision_rect.height = 10
        self.ground_colision_rect.y = y + self.colision_rect.height - 45

    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.colision_rect.x += delta_x
        self.ground_colision_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.colision_rect.y += delta_y
        self.ground_colision_rect.y += delta_y

    def attack(self, direction):
        if (self.animation != self.attack_r and self.animation != self.attack_l) and self.is_death == False:

            self.is_attack = True
            if direction == DIRECTION_R:
                self.animation = self.attack_r
            else:
                self.animation = self.attack_l
            self.frame = 0
    def death(self):
        if (self.animation != self.death_r and self.animation != self.death_l and self.is_death == True):
            
            if self.direction == DIRECTION_R:
                self.animation = self.death_r

            else:
                self.animation = self.death_l



    def collide_with_player(self, Knight_rect,Knight_direction, Knight_attack):
        if (self.colision_rect.colliderect(Knight_rect) and self.is_death == False):
            if (Knight_attack):
                self.health -= 1
                if (self.health == 0):
                    self.is_death = True
                    self.death()
            if(Knight_direction == DIRECTION_R):
                self.attack(DIRECTION_L)
                self.is_attack = True
                self.move_x = 0 
            else:
                self.attack(DIRECTION_R)
                self.is_attack = True
                self.move_x = 0 
           
        else:
            self.is_attack = False

    def do_move(self, delta_ms, lista_plataformas):
        if (self.is_death == False):
            self.tiempo_transcurrido_move += delta_ms
            if (self.tiempo_transcurrido_move >= 10):
                self.tiempo_transcurrido_move = 0

                if (not self.is_on_platform(lista_plataformas)):
                    if (self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
                else:
                    self.is_fall = False
                    self.change_x(self.move_x)
                    if self.contador <= 50 and self.is_attack == False and self.colision_rect.x >= 0:
                            self.move_x = -self.speed
                            self.animation = self.walk_l
                            self.direction = DIRECTION_L
                            self.contador += 1
                            self.is_attack = False
                    elif self.contador <= 100 and self.is_attack == False and self.colision_rect.x <= 1000:
                        self.move_x = self.speed
                        self.animation = self.walk_r
                        self.contador += 1
                        self.is_attack = False
                    else:
                        self.contador = 0

    def is_on_platform(self, lista_plataformas):
        retorno = False

        if (self.ground_colision_rect.bottom >= 800):
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if (self.ground_colision_rect.colliderect(plataforma.rect_ground_colision)):
                    retorno = True
                    break
        return retorno
        

    def do_animation(self, delta_ms):
            self.tiempo_transcurrido_animation += delta_ms
            if self.tiempo_transcurrido_animation >= 100:
                self.tiempo_transcurrido_animation = 0
                if self.is_death == True:
                    if self.frame < len(self.animation) - 1:
                        self.frame += 1
                else:
                    if self.frame < len(self.animation) - 1:
                        self.frame += 1
                    else:
                        self.frame = 0

    def update(self, delta_ms, lista_plataformas):
        self.do_move(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)

    def draw(self, screen):
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.colision_rect)
            pygame.draw.rect(screen, VERDE, self.ground_colision_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)


class Boss:
    def __init__(self, x, y, gravity, speed,is_death=False) -> None:
        self.walk_r = Auxillar.getSurfaceFromSpriteSheet("Recursos\Boss\Walk.png", 8, 1, True)
        self.walk_l = Auxillar.getSurfaceFromSpriteSheet("Recursos\Boss\Walk.png", 8, 1)
        self.attack_r = Auxillar.getSurfaceFromSpriteSheet("Recursos\Boss\Attack.png", 7, 1, True)
        self.attack_l = Auxillar.getSurfaceFromSpriteSheet("Recursos\Boss\Attack.png", 7, 1)
        self.contador = 0
        self.frame = 0
        self.health = 300
        self.move_x = 0
        self.move_y = 0
        self.speed = speed
        self.gravity = gravity
        self.animation = self.walk_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_jump = False
        self.is_fall = False
        self.is_attack = False
        self.is_death = is_death
        self.dead = False


        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.colision_rect = pygame.Rect(
            x+self.rect.width/3, y, self.rect.width/3, self.rect.height)
        self.ground_colision_rect = pygame.Rect(self.colision_rect)
        self.ground_colision_rect.height = 10
        self.ground_colision_rect.y = y + self.colision_rect.height

    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.colision_rect.x += delta_x
        self.ground_colision_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.colision_rect.y += delta_y
        self.ground_colision_rect.y += delta_y

    def attack(self, direction):
        if (self.animation != self.attack_r and self.animation != self.attack_l) and self.is_death == False:

            self.is_attack = True
            if direction == DIRECTION_R:
                self.animation = self.attack_r
            else:
                self.animation = self.attack_l
            self.frame = 0  
    
    
    def collide_with_player(self, Knight_rect,Knight_direction, Knight_attack):
        if (self.colision_rect.colliderect(Knight_rect) and self.is_death == False):
            if (Knight_attack):
                self.health -= 1
                if (self.health <= 0):
                    self.is_death = True
                    self.rect.x = -10000
                    self.rect.y = -10000
                    self.dead = True
            if(Knight_direction == DIRECTION_R):
                self.attack(DIRECTION_L)
                self.is_attack = True
                self.move_x = 0 
            else:
                self.attack(DIRECTION_R)
                self.is_attack = True
                self.move_x = 0 
           
        else:
            self.is_attack = False

    def do_move(self, delta_ms, lista_plataformas):
        if (self.is_death == False):
            self.tiempo_transcurrido_move += delta_ms
            if (self.tiempo_transcurrido_move >= 30):
                self.tiempo_transcurrido_move = 0

                
                if (not self.is_on_platform(lista_plataformas)):
                    if (self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
                else:
                    self.is_fall = False
                    self.change_x(self.move_x)
                    if self.contador <= 60 and self.is_attack == False:
                        self.move_x = -self.speed
                        self.animation = self.walk_l
                        self.direction = DIRECTION_L
                        self.contador += 1
                        self.is_attack = False
                    elif self.contador <= 120 and self.is_attack == False:
                        self.move_x = self.speed
                        self.animation = self.walk_r
                        self.contador += 1
                        self.is_attack = False
                    else:
                        self.contador = 0

    def is_on_platform(self, lista_plataformas):
        retorno = False

        if (self.ground_colision_rect.bottom >= 800):
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if (self.ground_colision_rect.colliderect(plataforma.rect_ground_colision)):
                    retorno = True
                    break
        return retorno

    def do_animation(self, delta_ms):
            self.tiempo_transcurrido_animation += delta_ms
            if self.tiempo_transcurrido_animation >= 120:
                self.tiempo_transcurrido_animation = 0
                if self.is_death == True:
                    if self.frame < len(self.animation) - 1:
                        self.frame += 1
                else:
                    if self.frame < len(self.animation) - 1:
                        self.frame += 1
                    else:
                        self.frame = 0

    def update(self, delta_ms, lista_plataformas):
        self.do_move(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)

    def draw(self, screen):
        if (DEBUG == True):
            pygame.draw.rect(screen, ROJO, self.colision_rect)
            pygame.draw.rect(screen, VERDE, self.ground_colision_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

