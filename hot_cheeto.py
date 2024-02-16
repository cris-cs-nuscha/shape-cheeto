""""
Nuscha Phraaruk 

I will code my program to draw many different shapes with different colors,
sizes, and positions. the instrunctions for each shapes will be read from a file 
"""

import turtle
import sys
from read_shapes import read_csv
    
def print_error(msg):
    """prints to stderr"""
    print(msg, file=sys.stderr)

# shape handler functions
def draw_square(t, data):
    '''Draws a square on given turtle object and data dictionary'''
    print(data)
    t.setpos(int(data['pos_x']), int(data['pos_y']))
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    #180-90=90

def draw_circle(t, data):
    '''Draws a circle on given turtle object and data dictionary'''
    print(data)
    print("draw_circle coming soon")

handlers = {
'square': draw_square,
'circle': draw_circle 
}

def get_handler(shape_type):
    """returns a handler function given a shapes string"""
    if shape_type in handlers:
        f = handlers[shape_type]
        return f
    else:
        print_error("no such type handler: " + data['type'])
        return None


# turtle object
win = turtle.Screen()
t = turtle.Turtle()
t.down()

# read shapes data file and call handler function for each shapes dictionary 
for data in read_csv():
    draw_f = get_handler(data['type'])
    if draw_f:
        draw_f(t, data) 


# # draw shapes to turtle object
# draw_square(t)

# t.screen.mainloop()