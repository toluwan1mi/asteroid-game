import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        
        # Giving the quit button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # Setting background colour to black

        pygame.display.flip() # Refreshing display


if __name__ == "__main__":
    main()
