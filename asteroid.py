import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
             log_event("asteroid_split")
             random_angle = random.uniform(20, 50)
             asteroid_1 = self.velocity.rotate(random_angle)
             asteroid_2 = self.velocity.rotate(-random_angle)
             self.radius = self.radius - ASTEROID_MIN_RADIUS
             asteroid_1_spawn = Asteroid(self.position.x, self.position.y, self.radius)
             asteroid_2_spawn = Asteroid(self.position.x, self.position.y, self.radius)
             asteroid_1_spawn.velocity = asteroid_1 * 1.2
             asteroid_2_spawn.velocity = asteroid_2 * 1.2
