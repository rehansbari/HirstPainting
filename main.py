# Using inspiration from Damien Hirst, an artist who frequently sells paintings for >1M USD, I wrote a Python Program
# that will create a painting that looks similar to the one of his multimillion dollar creations
# The painting will mimick the one found here https://www.newyorker.com/magazine/2012/01/23/spot-on
# This painting will be generated using the built in Turtle class that comes with Python.

import turtle
import random

import colorgram

#Extracting rgb colors from an image and placing them into a tuple
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

#Dot should be 20 in size, with 50 spaces in beween each dot
color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

#Creating the starting elements for the painting
timmy = turtle.Turtle()
turtle.colormode(255)
timmy.pu()
X_COORD = -300
Y_COORD = -200

#Generating random colors from the list
def set_color():
    random_color = random.choice(color_list)
    timmy.color(random_color)

#Moving the turtle across the screen horizontally 10 times
def horizontal():
    for _ in range(10):
        set_color()
        timmy.dot(20)
        timmy.fd(50)

#Starting the program, setting initial coordinates for turtle and calibrating y-coordinate by 50 with each passthrough
def start():
    global X_COORD
    global Y_COORD
    for _ in range(10):
        timmy.setx(X_COORD)
        timmy.sety(Y_COORD)
        horizontal()
        Y_COORD += 50

start()