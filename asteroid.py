from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.random_angle = random.uniform(20,50)
    
    def draw(self,screen):
        return pygame.draw.circle(screen,'white',self.position,self.radius,width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            pos = self.velocity.rotate(self.random_angle)
            neg = self.velocity.rotate(-1*(self.random_angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(x = self.position.x,y = self.position.y,radius=new_radius)
            asteroid2 = Asteroid(x = self.position.x,y = self.position.y,radius=new_radius)
            asteroid1.velocity= pos * 1.2
            asteroid2.velocity = neg*1.2
        
        