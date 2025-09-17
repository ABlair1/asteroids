import pygame
import constants


def get_screen() -> pygame.SurfaceType:
    screen = pygame.display.set_mode(
        size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
    )
    return screen

def game_loop(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

def main():
    pygame.init()

    print(constants.STARTUP_TEXT)

    game_loop(get_screen())


if __name__ == "__main__":
    main()
