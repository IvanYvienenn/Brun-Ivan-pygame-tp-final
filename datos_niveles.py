import pygame
import sys
from auxillar import Auxillar
from player import Player_1
from enemigo import Skeleton_enemy, Boss
from plataforma import *
from plataforma_dinamica import platform
from botin import *
from trampas import fuego, trampas
from constantes import *


def datos_nivel_1():
    Knight = Player_1(x=1270, y=150, gravity=6, jump_power=5, jump_height=200)

    lista_enemigos = []
    lista_enemigos.append(Skeleton_enemy(200, 150, gravity=6, speed=1))
    lista_enemigos.append(Skeleton_enemy(700, 150, gravity=6, speed=1))
    lista_enemigos.append(Skeleton_enemy(500, 350, gravity=6, speed=1))
    lista_enemigos.append(Skeleton_enemy(1000, 550, gravity=6, speed=1))


    lista_plataformas = []
    lista_plataformas.append(plataforma(0, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(50, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(100, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(150, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(200, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(250, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(300, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(350, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(400, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(450, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(500, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(550, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(600, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(650, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(700, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(750, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(800, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(850, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(900, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(950, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(1000, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(1050, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(1100, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(1150, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(1200, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(1250, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(1300, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(1350, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(0, 450, 50, 50, 0))
    lista_plataformas.append(plataforma(50, 450, 50, 50, 1))
    lista_plataformas.append(plataforma(100, 450, 50, 50, 2))
    lista_plataformas.append(plataforma(150, 450, 50, 50, 3))
    lista_plataformas.append(plataforma(200, 450, 50, 50, 0))
    lista_plataformas.append(plataforma(250, 450, 50, 50, 1))
    lista_plataformas.append(plataforma(300, 450, 50, 50, 2))
    lista_plataformas.append(plataforma(350, 450, 50, 50, 3))
    lista_plataformas.append(plataforma(400, 450, 50, 50, 0))
    lista_plataformas.append(plataforma(450, 450, 50, 50, 1))
    lista_plataformas.append(plataforma(500, 450, 50, 50, 2))
    lista_plataformas.append(plataforma(550, 450, 50, 50, 3))
    lista_plataformas.append(plataforma(600, 450, 50, 50, 0))
    lista_plataformas.append(plataforma(650, 450, 50, 50, 1))
    lista_plataformas.append(plataforma(700, 450, 50, 50, 2))
    lista_plataformas.append(plataforma(750, 450, 50, 50, 3))
    lista_plataformas.append(plataforma(800, 450, 50, 50, 0))
    lista_plataformas.append(plataforma(850, 450, 50, 50, 1))
    lista_plataformas.append(plataforma(900, 450, 50, 50, 2))
    lista_plataformas.append(plataforma(950, 450, 50, 50, 3))
    lista_plataformas.append(plataforma(1000, 450, 50, 50, 0))
    lista_plataformas.append(plataforma(1050, 450, 50, 50, 1))
    lista_plataformas.append(plataforma(1100, 450, 50, 50, 2))
    lista_plataformas.append(plataforma(1150, 450, 50, 50, 3))
    lista_plataformas.append(plataforma(1320, 450, 50, 50, 1))
    lista_plataformas.append(plataforma(100, 250, 50, 50, 2))
    lista_plataformas.append(plataforma(150, 250, 50, 50, 3))
    lista_plataformas.append(plataforma(200, 250, 50, 50, 0))
    lista_plataformas.append(plataforma(250, 250, 50, 50, 1))
    lista_plataformas.append(plataforma(300, 250, 50, 50, 2))
    lista_plataformas.append(plataforma(350, 250, 50, 50, 3))
    lista_plataformas.append(plataforma(400, 250, 50, 50, 0))
    lista_plataformas.append(plataforma(450, 250, 50, 50, 1))
    lista_plataformas.append(plataforma(500, 250, 50, 50, 2))
    lista_plataformas.append(plataforma(550, 250, 50, 50, 3))
    lista_plataformas.append(plataforma(600, 250, 50, 50, 0))
    lista_plataformas.append(plataforma(650, 250, 50, 50, 1))
    lista_plataformas.append(plataforma(700, 250, 50, 50, 2))
    lista_plataformas.append(plataforma(750, 250, 50, 50, 3))
    lista_plataformas.append(plataforma(800, 250, 50, 50, 0))
    lista_plataformas.append(plataforma(850, 250, 50, 50, 1))
    lista_plataformas.append(plataforma(900, 250, 50, 50, 2))
    lista_plataformas.append(plataforma(950, 250, 50, 50, 3))
    lista_plataformas.append(plataforma(1000, 250, 50, 50, 0))
    lista_plataformas.append(plataforma(1050, 250, 50, 50, 1))
    lista_plataformas.append(plataforma(1100, 250, 50, 50, 2))
    lista_plataformas.append(plataforma(1150, 250, 50, 50, 3))
    lista_plataformas.append(plataforma(1200, 250, 50, 50, 0))
    lista_plataformas.append(plataforma(1250, 250, 50, 50, 1))
    lista_plataformas.append(plataforma(1300, 250, 50, 50, 2))
    lista_plataformas.append(plataforma(1350, 250, 50, 50, 3))

    lista_plataformas_dinamicas = []

    lista_items = []
    lista_items.append(Health_up(800, 340))

    lista_items.append(coins(35, 250))
    lista_items.append(coins(35, 300))
    lista_items.append(coins(35, 350))

    lista_items.append(coins(1250, 500))
    lista_items.append(coins(1250, 550))
    lista_items.append(coins(1250, 600))

    lista_items.append(coins(300, 600))
    lista_items.append(coins(350, 600))

    lista_trampas = []
    lista_trampas.append(fuego(500, 620))
    lista_trampas.append(fuego(530, 620))
    lista_trampas.append(fuego(560, 620))
    lista_trampas.append(fuego(590, 620))
    lista_trampas.append(fuego(620, 620))

    return Knight, lista_enemigos, lista_plataformas, lista_items, lista_trampas, lista_plataformas_dinamicas


def datos_nivel_2():

    Knight = Player_1(x=1270, y=550, gravity=6, jump_power=5, jump_height=200)

    lista_enemigos = []
    lista_enemigos.append(Skeleton_enemy(1000, 550, gravity=6, speed=1))
    lista_enemigos.append(Skeleton_enemy(600, 550, gravity=6, speed=1))
    lista_enemigos.append(Skeleton_enemy(300, 550, gravity=6, speed=1))
    lista_enemigos.append(Skeleton_enemy(300, 200, gravity=6, speed=1))
    lista_enemigos.append(Skeleton_enemy(700, 200, gravity=6, speed=1))

    lista_plataformas = []
    lista_plataformas.append(plataforma(0, 650, 50, 50, 4))
    lista_plataformas.append(plataforma(50, 650, 50, 50, 4))
    lista_plataformas.append(plataforma(100, 650, 50, 50, 4))
    lista_plataformas.append(plataforma(150, 650, 50, 50, 4))
    lista_plataformas.append(plataforma(200, 650, 50, 50, 4))
    lista_plataformas.append(plataforma(250, 650, 50, 50, 4))
    lista_plataformas.append(plataforma(300, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(350, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(400, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(450, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(500, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(550, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(600, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(650, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(700, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(750, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(800, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(850, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(900, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(950, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(1000, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(1050, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(1100, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(1150, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(1200, 650, 50, 50, 0))
    lista_plataformas.append(plataforma(1250, 650, 50, 50, 1))
    lista_plataformas.append(plataforma(1300, 650, 50, 50, 2))
    lista_plataformas.append(plataforma(1350, 650, 50, 50, 3))
    lista_plataformas.append(plataforma(0, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(50, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(150, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(200, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(250, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(300, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(350, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(400, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(450, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(500, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(550, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(600, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(650, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(700, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(750, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(800, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(850, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(900, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(950, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(1000, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(1250, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(1300, 380, 50, 50, 0))
    lista_plataformas.append(plataforma(1350, 380, 50, 50, 0))

    lista_plataformas_dinamicas = []
    lista_plataformas_dinamicas.append(platform(100, 570, 50, 50,))
    lista_plataformas_dinamicas.append(platform(1300, 300, 50, 50,))

    lista_items = []
    lista_items.append(coins(120, 500))
    lista_items.append(coins(120, 450))
    lista_items.append(coins(120, 400))
    lista_items.append(coins(120, 350))
    lista_items.append(coins(1150, 200))
    lista_items.append(coins(1150, 250))
    lista_items.append(coins(1200, 250))
    lista_items.append(coins(1100, 200))
    lista_items.append(coins(1200, 200))
    lista_items.append(coins(1250, 200))

    lista_trampas = []
    lista_trampas.append(trampas(1100, 530))

    return Knight, lista_enemigos, lista_plataformas, lista_items, lista_trampas, lista_plataformas_dinamicas


def datos_nivel_3():
    Knight = Player_1(x=1250, y=700, gravity=6, jump_power=5, jump_height=200)

    lista_enemigos = []
    lista_enemigos.append(Boss(300, 375, 6, 2,))
    lista_enemigos.append(Skeleton_enemy(250, 550, 6, 1,))
    lista_enemigos.append(Skeleton_enemy(350, 550, 6, 1,))
    lista_enemigos.append(Skeleton_enemy(450, 550, 6, 1,))

    lista_plataformas = []
    lista_plataformas.append(plataforma_2(0, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(70, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(130, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(190, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(250, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(310, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(370, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(430, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(490, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(550, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(610, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(670, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(730, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(780, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(850, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(910, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(970, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(1030, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(1090, 600, 120, 120, 1))
    lista_plataformas.append(plataforma_2(1150, 600, 120, 120, 1))

    lista_plataformas_dinamicas = []
    lista_plataformas_dinamicas.append(platform(1230, 800, 50, 50,))
    lista_plataformas_dinamicas.append(platform(1280, 800, 50, 50,))

    lista_items = []
    lista_items.append(Health_up(1100, 430))

    lista_trampas = []

    return Knight, lista_enemigos, lista_plataformas, lista_items, lista_trampas, lista_plataformas_dinamicas
