import pygame
from constantes import *


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

jump_sound = pygame.mixer.Sound("Recursos\Knight\Sound\sfx_Jump.wav")
jump_sound.set_volume(0.5)

attack_sound = pygame.mixer.Sound("Recursos\Knight\Sound\sfx_Attack_1.wav")
attack_sound.set_volume(0.5)

fall_sound = pygame.mixer.Sound("Recursos\Knight\Sound\sfx_Fall.wav")
fall_sound.set_volume(0.5)

health_sound = pygame.mixer.Sound("Recursos\Musica\health.wav")
health_sound.set_volume(0.5)

coin_sound = pygame.mixer.Sound("Recursos\Musica\Coin.mp3")
coin_sound.set_volume(0.5)


def reproducir_musica(nivel):
    if nivel == "intro":
        pygame.mixer.music.load("Recursos\Musica\Menu.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    if nivel == "nivel_1":
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load("Recursos\Musica\Game.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    if nivel == "nivel_2":
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load("Recursos\Musica\Dance.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    if nivel == "nivel_3":
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load("Recursos\Musica\Boss.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
