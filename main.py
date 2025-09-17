import pygame
import constants


def get_screen() -> pygame.SurfaceType:
    screen = pygame.display.set_mode(
        size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
    )
    return screen

def game_loop(screen):
    # start clock for tracking framerate
    clock = pygame.time.Clock()
    dt = 0

    # begin game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(constants.FRAMERATE) / 1000  # delta time in seconds

def main():
    pygame.init()

    print(constants.STARTUP_TEXT)

    game_loop(get_screen())

    print(constants.SHUTDOWN_TEXT)


if __name__ == "__main__":
    main()
