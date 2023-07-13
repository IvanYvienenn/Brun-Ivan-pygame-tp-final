
import pygame
import sys
from constantes import *
from auxillar import *
from enemigo import *
from datos_niveles import *
from gui import *
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Plataformero")

class GameState():
    def __init__(self):
        self.state = "intro"
        self.intro_0 = True
        self.level_1 = False
        self.level_2 = False
        self.level_3 = False
        self.boss = False
        self.game_over = False
        self.win = False
        self.game_paused = False

    def intro(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass

            if (self.intro_0 == True):
                if resume_button.draw(screen):
                    game_state.state = "nivel_1"
                if button_audio.draw(screen):
                    if (pygame.mixer.music.get_volume() == 0):
                        pygame.mixer.music.set_volume(0.5)
                    else:
                        pygame.mixer.music.set_volume(0)
                if quit_button.draw(screen):
                    pygame.quit()
                    sys.exit()

        delta_ms = clock.tick(FPS)
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()

        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, (0, 0))

        draw_text("Score: " + str(Knight.score),
                  font, (0, 0, 0), 20, 20, screen)
        draw_text("Health: " + str(Knight.lives),
                  font, (0, 0, 0), 20, 50, screen)

        for plataforma in lista_plataformas:
            plataforma.draw(screen)

        for enemigo in lista_enemigos:
            enemigo.draw(screen)
            enemigo.update(delta_ms, lista_plataformas)
            enemigo.collide_with_player(
                Knight.rect, Knight.direction, Knight.is_attack)
            if (enemigo.is_death == True):
                lista_enemigos.remove(enemigo)

        for coin in lista_items:
            coin.draw(screen)
            coin.do_animation(delta_ms)

        for trampa in lista_trampas:
            trampa.draw(screen)
            trampa.do_animation(delta_ms)

        Knight.draw(screen)
        Knight.update(delta_ms, lista_plataformas, lista_plataformas_dinamicas)
        Knight.events(keys, delta_ms)
        Knight.knight_collide(lista_enemigos, lista_items,
                              lista_trampas, lista_plataformas_dinamicas)
        if (Knight.lives <= 0):
            game_state.lose()

        invisible_rect = pygame.Rect(20, 500, 50, 150)

        if (Knight.colision_rect.colliderect(invisible_rect)):
            lista_enemigos.clear()
            lista_items.clear()
            lista_plataformas.clear()
            lista_trampas.clear()

            game_state.state = "nivel_2"
        pygame.display.flip()

    def nivel_02(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, (0, 0))
        draw_text("Score: " + str(Knight.score),
                  font, (0, 0, 0), 20, 20, screen)
        draw_text("Health: " + str(Knight.lives),
                  font, (0, 0, 0), 20, 50, screen)

        for plataforma in lista_plataformas:
            plataforma.draw(screen)

        for plataforma_dinamica in lista_plataformas_dinamicas:
            plataforma_dinamica.draw(screen)
            plataforma_dinamica.do_animation(delta_ms)
            plataforma_dinamica.do_move(delta_ms)

        for enemigo in lista_enemigos:
            enemigo.draw(screen)
            enemigo.update(delta_ms, lista_plataformas)
            enemigo.collide_with_player(
                Knight.rect, Knight.direction, Knight.is_attack)
            if (enemigo.is_death == True):
                lista_enemigos.remove(enemigo)

        for coin in lista_items:
            coin.draw(screen)
            coin.do_animation(delta_ms)

        for trampa in lista_trampas:
            trampa.draw(screen)
            trampa.do_animation(delta_ms)

        Knight.draw(screen)
        Knight.update(delta_ms, lista_plataformas, lista_plataformas_dinamicas)
        Knight.events(keys, delta_ms)
        Knight.knight_collide(lista_enemigos, lista_items,
                              lista_trampas, lista_plataformas_dinamicas)
        invisible_rect = pygame.Rect(1250, 50, 150, 50)
        if (DEBUG == True):
            pygame.draw.rect(screen, (255, 0, 0), invisible_rect)
        if (Knight.colision_rect.colliderect(invisible_rect)):
            lista_enemigos.clear()
            lista_items.clear()
            lista_plataformas.clear()
            lista_trampas.clear()
            lista_plataformas_dinamicas.clear()

            game_state.state = "nivel_3"
        if (Knight.lives <= 0):
            game_state.lose()
        pygame.display.flip()

    def nivel_03(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, (0, 0))

        draw_text("Score: " + str(Knight.score),
                  font, (255, 255, 255), 20, 20, screen)
        draw_text("Health: " + str(Knight.lives),
                  font, (255, 255, 255), 20, 50, screen)

        for plataforma in lista_plataformas:
            plataforma.draw(screen)

        for plataforma_dinamica in lista_plataformas_dinamicas:
            plataforma_dinamica.draw(screen)
            plataforma_dinamica.do_animation(delta_ms)
            plataforma_dinamica.do_move(delta_ms)

        for enemigo in lista_enemigos:
            enemigo.draw(screen)
            enemigo.update(delta_ms, lista_plataformas)
            enemigo.collide_with_player(
                Knight.rect, Knight.direction, Knight.is_attack)
            if (type(enemigo) != Boss and enemigo.is_death == True):
                lista_enemigos.remove(enemigo)

        for coin in lista_items:
            coin.draw(screen)
            coin.do_animation(delta_ms)

        for trampa in lista_trampas:
            trampa.draw(screen)
            trampa.do_animation(delta_ms)

        Knight.draw(screen)
        Knight.update(delta_ms, lista_plataformas, lista_plataformas_dinamicas)
        Knight.events(keys, delta_ms)
        Knight.knight_collide(lista_enemigos, lista_items,
                              lista_trampas, lista_plataformas_dinamicas)

        invisible_rect_anti_fall = pygame.Rect(1200, 640, 200, 250)
        invisible_rect_boss = pygame.Rect(50, 0, 50, 700)
        if (Knight.colision_rect.colliderect(invisible_rect_anti_fall)):
            Knight.mover_y(-Knight.gravity)
        elif (Knight.colision_rect.colliderect(invisible_rect_boss)):
            Knight.score = 1500 + Knight.score
            game_state.winner()
        if (DEBUG == True):
            pygame.draw.rect(screen, (255, 0, 0), invisible_rect_anti_fall)
            pygame.draw.rect(screen, (255, 0, 0), invisible_rect_boss)
        if (Knight.lives <= 0):
            game_state.lose()

        pygame.display.flip()

    def lose(self,):
        # perdiste
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, (0, 0))
        draw_text("Game Over", font, (255, 255, 255), 500, 300, screen)
        draw_text("Score: " + str(Knight.score),
                  font, (255, 255, 255), 500, 350, screen)

    def winner(self):
        # ganaste
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, (0, 0))
        draw_text("You Win", font, (255, 255, 255), 500, 300, screen)
        draw_text("Score: " + str(Knight.score),
                  font, (255, 255, 255), 500, 350, screen)

    def GameStateManager(self):
        if self.state == "intro":
            self.intro()
        elif self.state == "nivel_1":
            self.main_game()
        elif self.state == "nivel_2":
            self.nivel_02()
        elif self.state == "nivel_3":
            self.nivel_03()


game_state = GameState()


if game_state.state == "intro" and game_state.intro_0 == True:
    reproducir_musica("intro")
    imagen_fondo = pygame.image.load(
        "Recursos\Background\Social\main_menu.jpg")
    screen.blit(imagen_fondo, (0, 0))
    resume_img = pygame.image.load(
        "Recursos/Pause/button_resume.png").convert_alpha()
    quit_img = pygame.image.load(
        "Recursos/Pause/button_quit.png").convert_alpha()
    back_img = pygame.image.load(
        "Recursos/Pause/button_back.png").convert_alpha()
    button_audio_img = pygame.image.load(
        "Recursos/Pause/button_audio.png").convert_alpha()
    font = pygame.font.Font("Recursos/Ariblk.ttf", 40)

    resume_button = button(50, 200, resume_img, 1)
    button_audio = button(50, 350, button_audio_img, 1)
    back_button = button(50, 400, back_img, 1)
    quit_button = button(50, 500, quit_img, 1)


# Game Loop
while True:

    game_state.GameStateManager()
    if (game_state.state == "intro" and game_state.intro_0 == False):
        reproducir_musica("intro")

    elif (game_state.state == "nivel_1" and game_state.level_1 == False):
        imagen_fondo = pygame.image.load(
            "Recursos/Background/Social/Proyecto.png")
        imagen_fondo = pygame.transform.scale(
            imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        screen.blit(imagen_fondo, (0, 0))
        reproducir_musica("nivel_1")
        game_state.level_1 = True
        Knight, lista_enemigos, lista_plataformas, lista_items, lista_trampas, lista_plataformas_dinamicas = datos_nivel_1()

    elif (game_state.state == "nivel_2" and game_state.level_2 == False):
        imagen_fondo = pygame.image.load(
            "Recursos/Background/Social/Test_2.png")
        imagen_fondo = pygame.transform.scale(
            imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        screen.blit(imagen_fondo, (0, 0))
        Knight, lista_enemigos, lista_plataformas, lista_items, lista_trampas, lista_plataformas_dinamicas = datos_nivel_2()
        reproducir_musica("nivel_2")
        game_state.level_2 = True
    elif (game_state.state == "nivel_3" and game_state.level_3 == False):
        imagen_fondo = pygame.image.load("Recursos/Background/Social/moon.png")
        imagen_fondo = pygame.transform.scale(
            imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        screen.blit(imagen_fondo, (0, 0))
        reproducir_musica("nivel_3")
        Knight, lista_enemigos, lista_plataformas, lista_items, lista_trampas, lista_plataformas_dinamicas = datos_nivel_3()
        game_state.level_3 = True
