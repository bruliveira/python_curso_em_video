#import webbrowser
#webbrowser.open('Destino.mp3')
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

Snake = [(200, 200), (210, 200), (220, 200)]
my_direction = LEFT



while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            pygame.display.update()
