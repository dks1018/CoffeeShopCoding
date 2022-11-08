import time

# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *


# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(10)

# Draw three circles:
draw_circle(tommy, "green", 50, 0, 100)
draw_circle(tommy, "green", 50, 0, 200)
draw_circle(tommy, "blue", 50, 75, 25)
draw_circle(tommy, "red", 50, -75, 25)

# Draw three Squares
draw_square(tommy, "green", 50, -50, -200)
draw_square(tommy, "green", 50, -50, -300)
draw_square(tommy, "blue", 50, 50, -200)
draw_square(tommy, "red", 50, -150, -200)

# Write a little message:
tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Darius's New Python Challenge", None, "center", "16pt 20")
tommy.goto(0,-80)

# Try changing draw_circle to draw_square, draw_triangle, or draw_star

#The turtle program is finished
turtle.done()

#Dont close out GUI for (x) seconds
#time.sleep(10)
