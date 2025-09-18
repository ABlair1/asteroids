import pygame


class CircleShape(pygame.sprite.Sprite):
    """
    Represents in-game objects with a circular shape
    """
    def __init__(self, x: int, y: int, radius: int):
        # TODO: if self has attribute 'containers', then pass into superclass init as arg
        super().__init__()

        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        """Must override in subclass"""
        raise NotImplementedError

    def update(self, dt: int):
        """Must override in subclass"""
        raise NotImplementedError
