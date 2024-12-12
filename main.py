# importing required files
import pygame
from constants import *
from player import Player


def main():
    # initalization of pygame
    pygame.init()   
    
    # creation of variables needed in main
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player.draw(screen)
        
        # Will update the contents of the entire display
        pygame.display.flip()
        
        # limits framerate to 60 FPS
        dt = clock.tick(60) /1000
    
    


if __name__ == "__main__":
    main()