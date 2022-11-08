import time

# I tweaked your code and read up a bit on the Turtle module to come up with my own design.
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *


# Create a turtle named Pancho(Pancho is a fitting name for him, he lives up at the top of the pyramid). Pancho is slow, like turtles are known to be.
Pancho = Turtle()
Pancho.shape("turtle")
Pancho.speed(5)


# Here is my design, obviously not a designer. But hey, i think it looks pretty cool. 
draw_square(Pancho, "red", 600, -600, -600)
draw_square(Pancho, "black", 400, -400, -400)
draw_square(Pancho, "yellow", 300, -300, -300)
draw_circle(Pancho, "yellow", 50, -340, 295)
draw_circle(Pancho, "yellow", 50, -340, -395)
draw_circle(Pancho, "yellow", 50, 340, -395)
draw_circle(Pancho, "yellow", 50, 340, 295)
draw_star(Pancho, "red", 20, 0, 335)
draw_star(Pancho, "red", 20, 0, -365)
draw_star(Pancho, "red", 20, 360, 0)
draw_star(Pancho, "red", 20, -340, 0)
draw_triangle(Pancho, "red", 200, -300, -300)
draw_triangle(Pancho, "black", 50, -75, 90)
draw_circle(Pancho, "yellow", 35, 0, 100)
draw_circle(Pancho, "black", 50, -245, 195)
draw_circle(Pancho, "yellow", 50, -245, 150)
draw_circle(Pancho, "black", 50, 245, 195)
draw_circle(Pancho, "yellow", 50, 245, 150)
draw_star(Pancho, "yellow", 85, 32, -175)
draw_square(Pancho, "black", 61.5, -60, -198)
draw_star(Pancho, "red", 30, 13, -160)
draw_circle(Pancho, "yellow", 25, 0, -170)
draw_square(Pancho, "black", 18, -18, -163)
draw_star(Pancho, "red", 8, 3, -150)
draw_circle(Pancho, "black", 7, 0, -153)
draw_circle(Pancho, "yellow", 3, 0, -149)
draw_star(Pancho, "black", 2, 1, -147 )
draw_circle(Pancho, "black", 50, -215, -300)
draw_circle(Pancho, "yellow", 35, -215, -285)
draw_circle(Pancho, "black", 20, -215, -270)
draw_circle(Pancho, "red", 5, -215, -255)
draw_circle(Pancho, "black", 50, 215, -300)
draw_circle(Pancho, "yellow", 35, 215, -285)
draw_circle(Pancho, "black", 20, 215, -270)
draw_circle(Pancho, "red", 5, 215, -255)
draw_circle(Pancho, "black", 25, 0, -290)
draw_circle(Pancho, "red", 25, 0, -270)
draw_circle(Pancho, "black", 15, 0, -260 )
draw_circle(Pancho, "black", 15, 0, 55)
draw_circle(Pancho, "red", 10, 0, 53)
draw_circle(Pancho, "black", 25, 80, -50)
draw_circle(Pancho, "red", 25, 60, -50)
draw_circle(Pancho, "black", 25, -80, -50)
draw_circle(Pancho, "red", 25, -60, -50)

# Write a little message:
Pancho.penup()
Pancho.goto(0,220)
Pancho.color("black")
Pancho.write("Russells Submission \n to Darius' Challenge", None, "center", font = ("times", 24, "bold"))
Pancho.goto(-1.5,135)
#Pancho returns home to the top of his super secret turtle illuminati pyramid. 
Pancho.color("green")

# As you can see I put in a whole boatload of circles and stars, some circles, and a couple triangles. I didn't really get around to messing with the shapes in the shapes file. 


#The turtle program is finished
turtle.done()

#Dont close out GUI for (x) seconds
time.sleep(10)
#This seems like a really cool module for python and there is alot you can do with it. I bookmarked the manual on my desktop for future reference. I plan on getting alot more proficient in coding sometime after we're done with class in june. 
 