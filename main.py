import pygame 
from constants import *
from player import Player,Shot
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    shots = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots, updatable, drawable)
    
    Player.containers = (updatable,drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player=Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    
    dt = 0

    print("Starting asteroids!")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        for t in updatable:
            t.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                return pygame.QUIT
            
        
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
           
            

        for d in drawable:
            d.draw(screen)
        
        
        pygame.display.flip()

        dt = clock.tick(60)/1000
        



if __name__ == "__main__":
    main()


