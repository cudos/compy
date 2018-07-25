#!/usr/bin/env python3

import vpython as vp
import numpy as np

planet_data = {
    "earth": {
        "orbit": 149.6,
        "period": 365.3,
        "radius": 6371.0,
    },
    "mercury": {
        "orbit": 57.9,
        "period": 88.0,
        "radius": 2440.0,
    },
    "venus": {
        "orbit":  108.2,
        "period": 224.7,
        "radius": 6052,
    },
    "mars": {
        "orbit":  227.9,
        "period": 687.0,
        "radius": 3386,
    },
    "jupiter": {
        "orbit": 778.5,
        "period": 4331.6,
        "radius": 69173,
    },
    "saturn": {
        "orbit": 1433.4,
        "period":  10759.2,
        "radius": 57316,
    },
}


class Planet(object):
    def __init__(self, orbit, period, radius):
        self.orbit = orbit * 1000.0 * 1000.0
        self.period = period
        self.radius = radius
        self.delta = 0
        if self.period != 0:
            self.delta = 2 * np.pi / self.period
        self.sphere = vp.sphere(
            pos=vp.vector(0, self.orbit, 0),
            radius=self.radius / 50.0
        )

    def update_position(self):
        pos = self.sphere.pos
        if pos.x > 0:
            phi = np.arctan(pos.y / pos.x)
        elif pos.x < 0 and pos.y >= 0:
            phi = np.arctan(pos.y / pos.x) + np.pi
        elif pos.x < 0 and pos.y < 0:
            phi = np.arctan(pos.y / pos.x) - np.pi
        elif pos.x == 0 and pos.y > 0:
            phi = np.pi / 2
        elif pos.x == 0 and pos.y < 0:
            phi = - np.pi / 2
        else:
            phi = 0

        self.sphere.pos = vp.vector(
            self.radius * np.cos(phi + self.delta),
            self.radius * np.sin(phi + self.delta),
            0
        )


# Setup sun
Planet(orbit=0, period=0, radius=1000)

# Setup planets
planets = []
for planet, data in planet_data.items():
    orbit = data["orbit"]
    radius = data["radius"]
    planet = Planet(
        orbit=data["orbit"], period=data["period"], radius=data["radius"]
    )
    planets.append(planet)

# Let'em move
while True:
    vp.rate(30)
    for planet in planets:
        planet.update_position()
