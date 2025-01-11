import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Asteroid(CircleShape):
    def __ini__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt