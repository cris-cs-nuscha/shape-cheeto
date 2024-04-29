""""
Nuscha Phraaruk 

I will code my program to draw many different shapes with different colors,
sizes, and positions. the instrunctions for each shapes will be read from a file 
"""
from random import*
import turtle
import sys

# turtle.pensize(3)
# turtle.circle(100)

# turtle.pensize(5)

# for i in range(5):
#     turtle.forward(300)
#     turtle.left(144)

# turtle.hideturtle()

# turtle.pensize(3)

# for i in range(3):
#     turtle.left(120)
#     turtle.forward(200)

# turtle.exitonclick()

from read_shapes import read_csv


def print_error(msg):
    """prints to stderr"""
    print(msg, file=sys.stderr)

# shape handler functions
def draw_rectangle(t, data):
    '''Draws a square on given turtle object and data dictionary'''
    if t.isdown():
        t.up()
    t.setpos(int(data['pos_x']), int(data['pos_y']))
    t.color(data['color'])
    t.fillcolor(data['fill']) 
    t.down()
    t.begin_fill()
    side1 = float(data["size1"])
    side2 = float(data["size2"])
    # iterate the four sides of a rectangle
    for s in (side1, side2, side1, side2):
        t.forward(s)
        t.left(90)
    t.end_fill()
    t.up()

def draw_square(t, data):
    """Use draw_rectangle to draw a square"""
    data['size2'] = data['size1']
    draw_rectangle(t, data)

def draw_triangle(t, data):
    '''Draws a square on given turtle object and data dictionary'''
    if t.isdown():
        t.up()
    t.setpos(int(data['pos_x']), int(data['pos_y']))
    t.color(data['color'])
    t.fillcolor(data['fill']) 
    t.down()
    t.begin_fill()
    side = float(data["size1"])
    for _ in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()
    t.up()


def draw_circle(t, data):
    '''Draws a circle on given turtle object and data dictionary'''
    if t.isdown():
        t.up()
    t.setpos(int(data['pos_x']), int(data['pos_y']))
    t.pencolor(data['color'])
    t.fillcolor(data['fill'])
    t.down()
    t.begin_fill()
    radius = float(data["size1"])
    t.color(data['color']) 
    t.circle(radius)
    '''Draws a square on given turtle object and data dictionary'''
    print("pendown:", t.isdown())
    t.end_fill()
    t.up()

# dictionary of shapes and callback functions 
handlers = {
    'rectangle': draw_rectangle,
    'square': draw_square,
    'circle': draw_circle,
    'triangle': draw_triangle
}

def get_handler(shape_type):
    """returns a handler function given a shapes string"""
    if shape_type in handlers:
        f = handlers[shape_type]
        return f
    else:
        print_error("no such type handler: " + data['type'])
        return None


# create turtle object and Screen
t = turtle.Turtle()
t.speed(9)
win = turtle.Screen()

#win.bgpic("grid.png")
t.up()

# read shapes data file and call handler function for each shapes dictionary 
for data in read_csv():
    draw_f = get_handler(data['type'])
    if draw_f:
        print("calling handler: " + data['type'])
        print(data)
        # call shape function (including student developed procedure "draw_rectangle")
        draw_f(t, data) 

t.hideturtle()
# keep window open until user closes it
turtle.exitonclick()