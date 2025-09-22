import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FRAMERATE,
    STARTUP_TEXT,
    SHUTDOWN_TEXT,
    GAME_OVER_TEXT,
)
from player import Player
from shot import Shot


def get_screen() -> pygame.Surface:
    screen = pygame.display.set_mode(
        size=(SCREEN_WIDTH, SCREEN_HEIGHT),
    )
    return screen

def game_over() -> None:
    print(GAME_OVER_TEXT)
    print(SHUTDOWN_TEXT)
    sys.exit()

def game_loop() -> None:
    # game setup
    screen = get_screen()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # begin game loop
    while True:
        # check for player input or game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # update display and in-game objects 
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # check for asteroid collisions
        for asteroid in asteroids:
            if player.has_collision(asteroid):
                game_over()
            for shot in shots:
                if asteroid.has_collision(shot):
                    asteroid.split()

        # update delta time in seconds based on framerate
        dt = clock.tick(FRAMERATE) / 1000

def main():
    pygame.init()

    print(STARTUP_TEXT)

    game_loop()

    print(SHUTDOWN_TEXT)


if __name__ == "__main__":
    main()
