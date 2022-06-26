#!.\env\Scripts\python
import pygame
import sys
from settings import *
from level import Level

# MINUTO 1:03:00


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zeld4')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            self.clock.tick(FPS)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
