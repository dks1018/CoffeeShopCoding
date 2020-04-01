import time

# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *


# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(9999999999999)

draw_square(turtle, "#1728BC", 350, -350, -400)


draw_square(turtle, "black", 4, -45, 290)
draw_square(turtle, "black", 4, -45, 280)
draw_square(turtle, "black", 4, -45, 270)
draw_square(turtle, "black", 4, -45, 260)
draw_square(turtle, "black", 4, -45, 250)
draw_square(turtle, "black", 4, -45, 240)
draw_square(turtle, "black", 4, -45, 230)
draw_square(turtle, "black", 4, -45, 220)
draw_square(turtle, "black", 4, -45, 210)
draw_square(turtle, "black", 4, -45, 200)
draw_square(turtle, "black", 4, -45, 190)
draw_square(turtle, "black", 4, -45, 180)
draw_square(turtle, "black", 4, -45, 170)
draw_square(turtle, "black", 4, -45, 160)
draw_square(turtle, "black", 4, -45, 150)
draw_square(turtle, "black", 4, -45, 140)
draw_square(turtle, "black", 4, -45, 130)
draw_square(turtle, "black", 4, -45, 120)
draw_square(turtle, "black", 4, -45, 110)
draw_square(turtle, "black", 3, -48, 105)
draw_square(turtle, "black", 3, -49, 103)
draw_square(turtle, "black", 3, -52, 100)
draw_square(turtle, "black", 3, -55, 100)
draw_square(turtle, "black", 3, -58, 100)
draw_square(turtle, "black", 3, -58, 100)
draw_square(turtle, "black", 3, -62, 103)
draw_square(turtle, "black", 3, -65, 106)
draw_square(turtle, "black", 3, -66, 109)


#Fish 1
draw_triangle1(turtle, "yellow", 12, -180, -80)
draw_triangle1(turtle, "#86AEFF", 25, -100, -100)
draw_triangle2(turtle, "#1E66F6", 25, -165, -62)
draw_triangle1(turtle, "blue", 10, -115, -75)

draw_circle(turtle, "white", "white", 5, -70, -65)
draw_circle(turtle, "black", "black", 2, -65, -60)
draw_triangle2(turtle, "#1728BC", 4, -45, -65)
#fish 2
draw_triangle2(turtle, "yellow", 20, 175, 80)
draw_triangle1(turtle, "green", 40, 80, 20)
draw_triangle2(turtle, "#11D037", 40, -25, 80)
draw_triangle2(turtle, "#8F54E8", 20, 45, 85)

draw_circle(turtle, "white", "white", 8, 10, 75)
draw_circle(turtle, "black", "black", 4, 5, 85)
draw_triangle1(turtle, "#1728BC", 5, -25, 72)
#bubbles
draw_circle(turtle, "white", "blue", 5, -185, -190)
draw_circle(turtle, "white", "blue", 10, -190, -170)
draw_circle(turtle, "white", "blue", 20, -240, -150)
draw_circle(turtle, "white", "blue", 35, -235, -100)
draw_circle(turtle, "white", "blue", 40, -200, 30)
draw_circle(turtle, "white", "blue", 25, -180, 95)
draw_circle(turtle, "white", "blue", 35, -200, 125)
draw_circle(turtle, "white", "blue", 25, -90, -0)
draw_circle(turtle, "white", "blue", 10, -100, 40)
draw_circle(turtle, "white", "blue", 15, -50, 0)
draw_circle(turtle, "white", "blue", 25, -255, -0)

#line and hook


# Write a little message:
tommy.penup()
tommy.goto(25,-200)
tommy.color("yellow")
tommy.write("Nope! Not today!", None, "center", "18pt 20")
tommy.goto(0,-300)

# Try changing draw_circle to draw_square, draw_triangle, or draw_star

#The turtle program is finished
turtle.done()

#Dont close out GUI for (x) seconds
#time.sleep(10)
