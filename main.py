import turtle
import math
import time
from typing import List

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulator")
screen.tracer(0)




#defines How Planets are made
class Planet:
    def __init__(self, name: str, shape: str, color: str, pos: list[float], vel: List[float], mass: float):
        self._name   = name
        self._shape  = shape
        self._color  = color
        self._pos = pos
        self._vel  = vel
        self._mass = mass
        
        self.turtle = turtle.Turtle()
        self.turtle.shape(self._shape)
        self.turtle.color(self._color)
        self.turtle.penup()
        self.turtle.goto(self._pos[0], self._pos[1])
        self.turtle.pendown()

        
    def update(self, other_bodies: List["Planet"], G: float, dt: float):
        ax = 0
        ay = 0

        for body in other_bodies:
            if body is self:
                continue

            dx = body._pos[0] - self._pos[0]
            dy = body._pos[1] - self._pos[1]
            distance = math.sqrt(dx**2 + dy**2)

            if distance == 0:
                continue  # Prevent divide by zero

            force_mag = G * body._mass / distance**2

            unit_dx = dx / distance
            unit_dy = dy / distance

            ax += force_mag * unit_dx
            ay += force_mag * unit_dy
            
            screen.update()

        self._vel[0] += ax * dt
        self._vel[1] += ay * dt

        self._pos[0] += self._vel[0] * dt
        self._pos[1] += self._vel[1] * dt

        self.turtle.goto(self._pos[0], self._pos[1])

    



sun = Planet("Sun", "circle", "yellow", [0, 0], [0, 0], mass=1000)
earth = Planet("Earth", "circle", "blue", [150, 0], [0, 2], mass=1)
mars  = Planet("Mars",  "circle", "red",  [250, 0], [0, 1.6], mass=0.11)


all_planets = [sun, earth, mars]
G = 0.9
dt = 0.05

while True:
    for planet in all_planets:
        planet.update(all_planets, G, dt)
        