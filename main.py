# simple python circle area calculator
# import modules

import math

# main class 
class Circle(object):
    """A simple circle area calculator"""
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2.0
    
"""Example use

c = Circle(10)

c.radius

c.area()
"""