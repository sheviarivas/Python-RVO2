#!/usr/bin/env python

import pygame
import sys

# Inicializar Pygame
pygame.init()
clock = pygame.time.Clock()

# Definir el tamaño de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Renderer")

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Función para generar agentes
def draw_agent(x, y, color):
    radio = 20
    pygame.draw.circle(screen, BLACK, (x, y), radio+3)  # Agente de radio r+3
    pygame.draw.circle(screen, color, (x, y), radio)  # Agente de radio r

# Abrir el archivo en modo lectura
with open('steps.txt', 'r') as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()

# Bucle principal del juego
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for linea in lineas:
            # Limpiar pantalla
            screen.fill(WHITE)

            # Divide la línea en columnas (suponiendo que están separadas por espacios)
            columnas = linea.split()
            
            # Procesa cada columna
            print("step: " + columnas[0])
            print("time: " + columnas[1])
            for i in range (2, len(columnas), 2):
                print("x: " + columnas[i] + " y: " + columnas[i+1])
                draw_agent(float(columnas[i])*100 + WIDTH/2, float(columnas[i+1])*100 + HEIGHT/2, RED)
                # pass

            # # Dibujar pelota en la posición dada por el usuario
            # for i in range(num_agents):
            #     x_input = input("Ingrese la posición x de la pelota: ")
            #     y_input = input("Ingrese la posición y de la pelota: ")

            #     draw_ball(float(x_input), float(y_input), RED)
            #     pass

            # Actualizar la pantalla
            pygame.display.flip()
            clock.tick(5)
            

# Ejecutar el juego
if __name__ == "__main__":
    main()
