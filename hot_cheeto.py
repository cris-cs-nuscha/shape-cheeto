""""
Nuscha Phraaruk 

I will code my program to draw many different shapes with different colors,
sizes, and positions. the instrunctions for each shapes will be read from a file 
"""

import turtle

def draw_square(t):
    "Draws a square on given turle object"
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    #180-90=90

# turtle object
win = turtle.Screen()
t = turtle.Turtle()
t.down()

# draw shapes to turtle object
draw_square(t)

t.screen.mainloop()
