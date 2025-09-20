import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    dt = 0


    # Game Loop
    while True:
        
        # Giving the quit button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        updatable.update(dt)

        for obj in asteroid:
            if obj.detect_collision(player):
                print("Game over!")
                return False
        
        screen.fill("black") # Setting background colour to black
        
        for obj in drawable:
            obj.draw(screen) # re-render the player each frame
        
        pygame.display.flip() # Refreshing display
        
        dt = game_clock.tick(60) / 1000 # limit fps to 60


if __name__ == "__main__":
    main()
