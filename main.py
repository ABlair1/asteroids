import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FRAMERATE,
    STARTUP_TEXT,
    SHUTDOWN_TEXT,
)
from player import Player


def get_screen() -> pygame.Surface:
    screen = pygame.display.set_mode(
        size=(SCREEN_WIDTH, SCREEN_HEIGHT),
    )
    return screen

def game_loop() -> None:
    screen = get_screen()
    # start clock for tracking framerate
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # begin game loop
    while True:
        # check for player input or game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # update display on screen
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(FRAMERATE) / 1000  # delta time in seconds

def main():
    pygame.init()

    print(STARTUP_TEXT)

    game_loop()

    print(SHUTDOWN_TEXT)


if __name__ == "__main__":
    main()
