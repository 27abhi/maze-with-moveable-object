# MAZE DESIGN & IMPLEMENTATION WITH KEYBOARD CONTROLLED MOVEABLE OBJECT (USING TURTLE FOR GRAPHICS):
#===================================================================================================

import numpy as np
import turtle
import random

window = turtle.Screen()
window.bgcolor('black')
window.screensize(600,600)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)
    


alex = turtle.Turtle()
alex.setpos(-216,288)
alex.right(90)
alex.color('yellow')
alex.penup()
alex.shape('circle')
    

walls=[]


#maze layout below can be manually modified:

layout = [
    "XXX XXXXXXXXXXXXXXXXXXXX",
    "XXX   XXX    XXXXXXXXXXX",
    "XXX  XXXXXXX      XXXXXX",
    "XXX   XXXXXXXXXXX XXXXXX",
    "XXX        XXXXXX     XX",
    "XXXXXX  XXXXXXXXX XXX XX",
    "XXXXXX            XXX XX",
    "XXXXXXX XXXXXXXXXXXXX  X",
    "XXXXXXX     XXXXXXXXXX X",
    "XXXXXXX XX XXXXXXX     X",
    "XXX     XX XXXXXXX XXX X",
    "XX  XXXXXX    XXXX XXXXX",
    "XX XXXXXXXXXX XX XXXXXXX",
    "X     XXXXXXX    XXXXXXX",
    "XX X      XXXX XXXXXXXXX",
    "XX XX XXX XXXX XXXXXXXXX",
    "XX XX  XX    X     XXXXX",
    "XX XXX XXXXXXXXXXX XXXXX",
    "XXXXXX XXXXXXXXXXX XXXXX",
    "XXXXXX  XXXXXXXXXX XXXXX",
    "XXX XXX XXXXXXXXXX XXXXX",
    "XXX          XXXXX XXXXX",
    "XXXXXXXXXXXXXXXXXX XXXXX",
    
]


#maze generating function:

def setup_maze(input_layout):
    for y in range(len(input_layout)):
        for x in range(len(input_layout[y])):
            character = input_layout[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character =="X":
                pen.goto(screen_x, screen_y)
                walls.append((screen_x, screen_y))
                pen.stamp()
                
pen = Pen()
setup_maze(layout)



#keyboard binding definitions for moving the object:

def h1():
    new_x_up = round(alex.xcor())
    new_y_up = round(alex.ycor() + 24)
    
    if(new_x_up, new_y_up) not in walls:
        alex.goto(new_x_up, new_y_up)
        
    
def h2():
    new_x_left = round(alex.xcor() - 24)
    new_y_left = round(alex.ycor())
    
    if(new_x_left, new_y_left) not in walls:
        alex.goto(new_x_left, new_y_left)
 
def h3():
    new_x_right = round(alex.xcor() + 24)
    new_y_right = round(alex.ycor())
    
    if(new_x_right, new_y_right) not in walls:
        alex.goto(new_x_right, new_y_right)
 
def h4():
    new_x_down = round(alex.xcor())
    new_y_down = round(alex.ycor() - 24)
    
    if(new_x_down, new_y_down) not in walls:
        alex.goto(new_x_down, new_y_down) 


window.onkey(h1, "Up")
window.onkey(h2, "Left")
window.onkey(h3, "Right")
window.onkey(h4, "Down")
window.listen()
turtle.mainloop()

while True:
    pass
    
    turtle.done()
   
    

    

