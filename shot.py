import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS


class Shot(CircleShape):
    """
    Represents a bullet shot from a ship.
    """
    def __init__(self, x: int, y: int, radius: int=SHOT_RADIUS):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def set_velocity(self, rotation: int, shoot_speed: int=PLAYER_SHOOT_SPEED):
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * shoot_speed

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
