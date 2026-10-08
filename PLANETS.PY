import turtle
import math
import time

# =========================
# SCREEN SETUP
# =========================

screen = turtle.Screen()
screen.setup(1100, 800)
screen.bgcolor("black")
screen.title("🌌 Solar System Animation")
screen.tracer(0)


# =========================
# STAR BACKGROUND
# =========================

stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.speed(0)

star_positions = [
    (-500, 300), (-420, 250), (-350, 320), (-280, 200),
    (-200, 300), (-100, 250), (20, 320), (120, 260),
    (220, 320), (330, 250), (450, 300), (500, 180),
    (-480, 100), (-390, 50), (-300, 120), (-180, 80),
    (-80, 130), (80, 70), (180, 130), (300, 80),
    (400, 140), (480, 60), (-450, -100), (-350, -180),
    (-250, -120), (-150, -200), (-50, -150), (100, -180),
    (200, -120), (320, -190), (420, -100), (500, -220),
    (-450, -300), (-300, -280), (-180, -330), (-50, -290),
    (100, -330), (250, -300), (380, -340), (480, -280)
]

for x, y in star_positions:
    stars.goto(x, y)
    stars.dot(3, "white")


# =========================
# SUN
# =========================

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3.5)
sun.penup()
sun.goto(0, 0)


# Sun label
sun_label = turtle.Turtle()
sun_label.hideturtle()
sun_label.color("white")
sun_label.penup()
sun_label.goto(-25, -55)
sun_label.write("SUN", font=("Arial", 12, "bold"))


# =========================
# PLANET DATA
# =========================

planets = [
    # name, color, distance, size, speed
    ("Mercury", "gray", 70, 0.7, 4.0),
    ("Venus", "orange", 110, 1.0, 3.0),
    ("Earth", "blue", 155, 1.1, 2.4),
    ("Mars", "red", 200, 0.9, 2.0),
    ("Jupiter", "orange", 260, 2.4, 1.2),
    ("Saturn", "gold", 330, 2.1, 0.9),
    ("Uranus", "lightblue", 395, 1.5, 0.7),
    ("Neptune", "blue", 455, 1.5, 0.5)
]


# =========================
# ORBIT LINES
# =========================

orbit_turtles = []

for name, color, distance, size, speed in planets:

    orbit = turtle.Turtle()
    orbit.hideturtle()
    orbit.speed(0)
    orbit.penup()
    orbit.goto(0, -distance)
    orbit.pendown()
    orbit.circle(distance)

    orbit_turtles.append(orbit)


# =========================
# CREATE PLANETS
# =========================

planet_objects = []

for name, color, distance, size, speed in planets:

    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()

    # Starting angle
    angle = 0

    planet_objects.append(
        {
            "object": planet,
            "name": name,
            "distance": distance,
            "speed": speed,
            "angle": angle
        }
    )


# =========================
# PLANET LABELS
# =========================

labels = []

for data in planet_objects:

    label = turtle.Turtle()
    label.hideturtle()
    label.color("white")
    label.penup()

    labels.append(label)


# =========================
# SATURN RING
# =========================

saturn_ring = turtle.Turtle()
saturn_ring.hideturtle()
saturn_ring.color("white")
saturn_ring.pensize(2)


# =========================
# EARTH MOON
# =========================

moon = turtle.Turtle()
moon.shape("circle")
moon.color("white")
moon.shapesize(0.35)
moon.penup()

moon_angle = 0


# =========================
# ANIMATION
# =========================

while True:

    earth_x = 0
    earth_y = 0

    for i, data in enumerate(planet_objects):

        planet = data["object"]
        distance = data["distance"]
        speed = data["speed"]

        # Increase angle
        data["angle"] += speed

        angle = math.radians(data["angle"])

        # Calculate planet position
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)

        planet.goto(x, y)

        # Planet label
        labels[i].clear()
        labels[i].goto(x - 20, y + 15)
        labels[i].write(
            data["name"],
            font=("Arial", 8, "normal")
        )

        # Save Earth position
        if data["name"] == "Earth":
            earth_x = x
            earth_y = y

        # Saturn ring
        if data["name"] == "Saturn":

            saturn_ring.clear()

            saturn_ring.penup()
            saturn_ring.goto(x - 35, y)

            saturn_ring.setheading(0)

            saturn_ring.pendown()

            for _ in range(2):
                saturn_ring.forward(70)
                saturn_ring.backward(70)

    # =========================
    # MOON MOVEMENT
    # =========================

    moon_angle += 8

    moon_radians = math.radians(moon_angle)

    moon_x = earth_x + 22 * math.cos(moon_radians)
    moon_y = earth_y + 22 * math.sin(moon_radians)

    moon.goto(moon_x, moon_y)

    # Update screen
    screen.update()

    time.sleep(0.02)