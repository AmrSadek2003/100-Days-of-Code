import turtle
import random
import colorgram

from turtle import Turtle, Screen
from random import randint
from colorgram import extract

turtle.colormode(255)

color_list = []

colors = colorgram.extract(r'C:\Users\amrsa\Desktop\hirst.jpg', 10)

for i in range(0, len(colors)):
    new_color = colors[i].rgb
    color_tuple = (new_color.r, new_color.g, new_color.b)
    color_list.append(color_tuple)


def randomcolor():
    color_tup = random.choice(color_list)
    return color_tup


def print_row(dot_color):
    current_pos = turtle.position()
    for z in range(10):
        dot_color = randomcolor()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.dot(20, dot_color)
    turtle.penup()
    turtle.setposition(current_pos[0], current_pos[1] + 50)
    turtle.pendown()


for x in range(10):
    print_row(randomcolor())

screen = Screen()
screen.exitonclick()
