import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulator")
screen.setup(width=900, height=900)

# Draw the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(stretch_wid=3, stretch_len=3)
sun.penup()
sun.goto(0, 0)

# Planet data: (name, color, orbit_radius, size, orbital_period_in_earth_years)
planets = [
    ("Mercury", "gray", 60, 0.3, 0.24),
    ("Venus", "orange", 90, 0.5, 0.62),
    ("Earth", "blue", 120, 0.6, 1.0),
    ("Mars", "red", 150, 0.5, 1.88),
    ("Jupiter", "brown", 200, 1.2, 11.86),
    ("Saturn", "gold", 250, 1.1, 29.46),
    ("Uranus", "light blue", 300, 0.9, 84.01),
    ("Neptune", "purple", 350, 0.9, 164.8)
]

# Calculate speed so that Earth completes a circle in 360 steps
base_speed = 3  # You can adjust this for animation speed
planet_turtles = []
speeds = []
for name, color, orbit_radius, size, period in planets:
    t = turtle.Turtle()
    t.shape("circle")
    t.color(color)
    t.shapesize(stretch_wid=size, stretch_len=size)
    t.penup()
    t.goto(orbit_radius, 0)
    t.pendown()
    t.speed(0)
    planet_turtles.append(t)
    speeds.append(base_speed / period)

# Draw orbits
orbit_drawer = turtle.Turtle()
orbit_drawer.hideturtle()
orbit_drawer.speed(0)
orbit_drawer.color("white")
orbit_drawer.penup()
for _, _, orbit_radius, _, _ in planets:
    orbit_drawer.goto(0, -orbit_radius)
    orbit_drawer.pendown()
    orbit_drawer.circle(orbit_radius)
    orbit_drawer.penup()

# Animate the planets
angles = [0] * len(planets)
while True:
    for i, (name, color, orbit_radius, size, speed) in enumerate(planets):
        angles[i] = (angles[i] + speeds[i]) % 360
        x = orbit_radius * math.cos(math.radians(angles[i]))
        y = orbit_radius * math.sin(math.radians(angles[i]))
        planet_turtles[i].goto(x, y)
    screen.update()
    time.sleep(0.02)

# To exit, close the turtle graphics window