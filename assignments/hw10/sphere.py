"""Name: Joshua Bee son
<hw1.py>
Problem: create a 3d sphere class
I certify that this assignment is entirely my own work."""
import math

class Sphere:
    """class for creating a sphere"""
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return float((4 * math.pi) * (self.radius ** 2))

    def volume(self):
        return float(((4/3) * math.pi) * (self.radius ** 3))
