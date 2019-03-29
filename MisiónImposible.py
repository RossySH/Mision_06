# Rosalía Serrano Herrera
# Dibuja como un esporógrafo

import pygame
import math

ANCHO = 700
ALTO = 700
# Colores
BLANCO = (255, 255, 255)
AZUL = (100,149,237)
MORADO = (154,50,205)
NEGRO = (0, 0, 0)
VERDE = (154, 205, 50)
NARANJA = (255, 160, 0)


def dibujar(r, R, l, r2, R2, l2):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        k = r / R
        for theta in range(0, 361*r//math.gcd(r, R)):
            a = math.radians(theta)
            x = int(R*((((1-k)*math.cos(a))+(l*k*math.cos(((1-k)/k)*a)))))
            y = int(R*((((1-k)*math.sin(a))-(l*k*math.sin(((1-k)/k)*a)))))
            pygame.draw.circle(ventana, NARANJA, (x+ANCHO//2, ALTO//2-y), 1)

        k2 = r2 / R2
        for theta2 in range(0, 361 * r2 // math.gcd(r2, R2)):
            b = math.radians(theta2)
            x2 = int(R2 * ((((1 - k2) * math.cos(b)) + (l * k2 * math.cos(((1 - k2) / k2) * b)))))
            y2 = int(R2 * ((((1 - k2) * math.sin(b)) - (l * k2 * math.sin(((1 - k2) / k2) * b)))))
            pygame.draw.circle(ventana, VERDE, (x2 + ANCHO // 2, ALTO // 2 - y2), 1)

        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()


def main():
    r = int(input("Teclea el valor de r: "))
    R = int(input("Teclea el valor de R: "))
    l = float(input("Teclea el valor de l: "))
    r2 = int(input("Teclea otro valor de r: "))
    R2 = int(input("Teclea otro valor de R: "))
    l2 = float(input("Teclea otro valor de l: "))
    dibujar(r, R, l, r2, R2, l2)


main()