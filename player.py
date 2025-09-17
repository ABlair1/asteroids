import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from typing import List


class Player(CircleShape):
    """
    Represents the player's ship. The ship will be displayed as a triangle,
    but its hitbox area will be that of a circle.
    """
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    def triangle(self) -> List[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen, 
            color="white",
            points=self.triangle(),
            width=2
        )