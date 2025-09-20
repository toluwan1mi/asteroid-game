import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # Game Loop
    while True:
        
        # Giving the quit button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # Setting background colour to black
        pygame.display.flip() # Refreshing display
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
