import pygame


class Auxillar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas, flip=False):
        lista = []
        imagen = pygame.image.load(path).convert_alpha()
        fotograma_ancho = int(imagen.get_width()/columnas)
        fotograma_alto = int(imagen.get_height()/filas)
        for fila in range(filas):
            for columna in range(columnas):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = imagen.subsurface(
                    x, y, fotograma_ancho, fotograma_alto)
                if flip:
                    surface_fotograma = pygame.transform.flip(
                        surface_fotograma, True, False)
                lista.append(pygame.transform.scale2x(surface_fotograma))

        return lista
