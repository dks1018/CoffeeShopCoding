import time

# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *

setup(width=1.00, height=1.00, startx=None, starty=None)
# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.hideturtle()
tommy.speed(750)

draw_square(tommy, "blue", 1000, -775, -400)
draw_square(tommy, "brown", 50, -775, -400)
draw_square_outline(tommy, "black", 50, -775, -400)
draw_square(tommy, "brown", 50, -675, -400)
draw_square_outline(tommy, "black", 50, -675, -400)
draw_square(tommy, "brown", 50, -575, -400)
draw_square_outline(tommy, "black", 50, -575, -400)
draw_square(tommy, "brown", 50, -475, -400)
draw_square_outline(tommy, "black", 50, -475, -400)
draw_square(tommy, "brown", 50, -375, -400)
draw_square_outline(tommy, "black", 50, -375, -400)
draw_square(tommy, "brown", 50, -275, -400)
draw_square_outline(tommy, "black", 50, -275, -400)
draw_square(tommy, "brown", 50, -175, -400)
draw_square_outline(tommy, "black", 50, -175, -400)
draw_square(tommy, "brown", 50, -75, -400)
draw_square_outline(tommy, "black", 50, -75, -400)
draw_square(tommy, "brown", 50, 25, -400)
draw_square_outline(tommy, "black", 50, 25, -400)
draw_square(tommy, "brown", 50, 125, -400)
draw_square_outline(tommy, "black", 50, 125, -400)
draw_square(tommy, "brown", 50, 225, -400)
draw_square_outline(tommy, "black", 50, 225, -400)
draw_square(tommy, "brown", 50, 325, -400)
draw_square_outline(tommy, "black", 50, 325, -400)
draw_square(tommy, "brown", 50, 425, -400)
draw_square_outline(tommy, "black", 50, 425, -400)
draw_square(tommy, "brown", 50, 525, -400)
draw_square_outline(tommy, "black", 50, 525, -400)
draw_square(tommy, "brown", 50, 625, -400)
draw_square_outline(tommy, "black", 50, 625, -400)
draw_square(tommy, "brown", 50, 725, -400)
draw_square_outline(tommy, "black", 50, 725, -400)

draw_square(tommy, "brown", 50, -775, -300)
draw_square_outline(tommy, "black", 50, -775, -300)
draw_square(tommy, "brown", 50, -675, -300)
draw_square_outline(tommy, "black", 50, -675, -300)
draw_square(tommy, "brown", 50, -575, -300)
draw_square_outline(tommy, "black", 50, -575, -300)
draw_square(tommy, "brown", 50, -475, -300)
draw_square_outline(tommy, "black", 50, -475, -300)
draw_square(tommy, "brown", 50, -375, -300)
draw_square_outline(tommy, "black", 50, -375, -300)
draw_square(tommy, "brown", 50, -275, -300)
draw_square_outline(tommy, "black", 50, -275, -300)
draw_square(tommy, "brown", 50, -175, -300)
draw_square_outline(tommy, "black", 50, -175, -300)
draw_square(tommy, "brown", 50, -75, -300)
draw_square_outline(tommy, "black", 50, -75, -300)
draw_square(tommy, "brown", 50, 25, -300)
draw_square_outline(tommy, "black", 50, 25, -300)
draw_square(tommy, "brown", 50, 125, -300)
draw_square_outline(tommy, "black", 50, 125, -300)
draw_square(tommy, "brown", 50, 225, -300)
draw_square_outline(tommy, "black", 50, 225, -300)
draw_square(tommy, "brown", 50, 325, -300)
draw_square_outline(tommy, "black", 50, 325, -300)
draw_square(tommy, "brown", 50, 425, -300)
draw_square_outline(tommy, "black", 50, 425, -300)
draw_square(tommy, "brown", 50, 525, -300)
draw_square_outline(tommy, "black", 50, 525, -300)
draw_square(tommy, "brown", 50, 625, -300)
draw_square_outline(tommy, "black", 50, 625, -300)
draw_square(tommy, "brown", 50, 725, -300)
draw_square_outline(tommy, "black", 50, 725, -300)

draw_square(tommy, "green", 20, 550, -200)
draw_square(tommy, "green", 20, 585, -200)
draw_square(tommy, "green", 20, 625, -200)
draw_square(tommy, "green", 20, 550, -165)
draw_square(tommy, "green", 20, 585, -165)
draw_square(tommy, "green", 20, 625, -165)
draw_square(tommy, "green", 30, 525, -130)
draw_square(tommy, "green", 30, 585, -130)
draw_square(tommy, "green", 30, 625, -130)

draw_triangle(tommy, "green", 50, -775, -200)
draw_triangle(tommy, "green", 50, -675, -200)
draw_square(tommy, "green", 50, -700, -170)
draw_circle(tommy, "green", 50, -650, -130)

draw_triangle(tommy, "green", 30, -85, -200)
draw_triangle(tommy, "green", 30, -15, -200)
draw_square(tommy, "green", 35, -40, -195)
draw_circle(tommy, "green", 35, -5, -165)

draw_square(tommy, "tan", 35, -175, -25)
draw_square_outline(tommy, "black", 35, -175, -25)
tommy.penup()
tommy.color("black")
tommy.goto(-140, -15)
tommy.write("?", None, "center", "25pt 35")
draw_square(tommy, "brown", 35, 15, -25)
draw_square_outline(tommy, "black", 35, 15, -25)
draw_bricks(15, -25)
draw_square(tommy, "tan", 35, 85, -25)
draw_square_outline(tommy, "black", 35, 85, -25)
tommy.penup()
tommy.color("black")
tommy.goto(120, -15)
tommy.write("?", None, "center", "25pt 35")
draw_square(tommy, "brown", 35, 155, -25)
draw_square_outline(tommy, "black", 35, 155, -25)
draw_bricks(155, -25)
draw_square(tommy, "tan", 35, 225, -25)
draw_square_outline(tommy, "black", 35, 225, -25)
tommy.penup()
tommy.color("black")
tommy.goto(260, -15)
tommy.write("?", None, "center", "25pt 35")
draw_square(tommy, "brown", 35, 295, -25)
draw_square_outline(tommy, "black", 35, 295, -25)
draw_bricks(295, -25)
draw_square(tommy, "tan", 35, 155, 165)
draw_square_outline(tommy, "black", 35, 155, 165)
tommy.penup()
tommy.color("black")
tommy.goto(190, 175)
tommy.write("?", None, "center", "25pt 35")
tommy.penup()
draw_mushroom(117.5, 70)
draw_goomba(175, -172)
draw_mario(-650, -140)

# Write a little message:
tommy.penup()
tommy.goto(-600,350)
tommy.color("white")
tommy.write("MARIO", None, "center", "35pt 30")
tommy.goto(-600,320)
tommy.write("000000", None, "center", "35pt 30")
tommy.goto(-200, 350)
tommy.pendown()
draw_circle(tommy, "gold", 20, -267.5, 355)
tommy.penup()
tommy.goto(-200, 350)
tommy.color("white")
tommy.write("x 00", None, "center", "35pt 30")
tommy.goto(200,350)
tommy.color("white")
tommy.write("WORLD", None, "center", "35pt 30")
tommy.goto(200,320)
tommy.write("1-1", None, "center", "35pt 30")
tommy.goto(600,350)
tommy.color("white")
tommy.write("TIME", None, "center", "35pt 30")
tommy.goto(600,320)
tommy.write("400", None, "center", "35pt 30")
# Try changing draw_circle to draw_square, draw_triangle, or draw_star

#The turtle program is finished
turtle.done()

#Dont close out GUI for (x) seconds
time.sleep(10)
