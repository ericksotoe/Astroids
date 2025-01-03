import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)

        
        for obj in asteroids:
            if obj.crash(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.crash(obj):
                    shot.kill()
                    obj.split()

        pygame.display.flip()
        

        # limit framerate to 60FPS
        dt = clock.tick(60.0) / 1000

        

        
    
    

if __name__ == "__main__":
    main()