import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from typing import List
from shot import Shot


class Player(CircleShape):
    """
    Represents the player's ship. The ship will be displayed as a triangle,
    but its hitbox area will be that of a circle.
    """
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self) -> List[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(
            surface=screen, 
            color="white",
            points=self.triangle(),
            width=2
        )

    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: int) -> None:
        # calculate direction Player is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # move forward based on speed
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self) -> Shot:
        shot = Shot(self.position.x, self.position.y)
        shot.set_velocity(self.rotation)
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        return shot

    def update(self, dt: int) -> None:
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            # 'a' key and left arrow rotates Player left
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            # 'd' key and right arrow rotates Player right
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            # 'w' key and up arrow move Player forward
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            # 's' key and down arrow move Player backward
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()
