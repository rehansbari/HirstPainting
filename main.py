# Using inspiration from Damien Hirst, an artist who frequently sells paintings for >1M USD, I wrote a Python Program
# that will create a painting that looks similar to the one of his multimillion dollar creations
# The painting will mimick the one found here https://www.newyorker.com/magazine/2012/01/23/spot-on
# This painting will be generated using the built in Turtle class that comes with Python.

from turtle import Turtle, Screen
import random

import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)











screen = Screen()
screen.exitonclick()