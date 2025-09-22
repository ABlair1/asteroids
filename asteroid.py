import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """
    Represents an asteroid.
    """
    def __init__(
        self, 
        x: int, 
        y: int, 
        radius: int, 
        velocity: pygame.math.Vector2
    ):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def split(self):
        self.kill() # destroy current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # spawn new, faster asteroids if current was not smallest size
        new_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(new_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-new_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity_1)
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity_2)
        


    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
