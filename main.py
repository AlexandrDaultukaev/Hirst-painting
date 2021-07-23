import math
import turtle as t
import random
import colorgram
sc = t.Screen()
t.colormode(255)
tim = t.Turtle()
colors = colorgram.extract("hirst_art/HirstArt.jpg", 15)
t.setworldcoordinates(0, 0, sc.window_width(), sc.window_height())
tim.pensize(30)

#move forward and draw one circle
def draw_circle():
    rand_choice = random.choice(colors)
    tup = (rand_choice.rgb[0], rand_choice.rgb[1], rand_choice.rgb[2])
    tim.penup()
    tim.forward(50)
    tim.pencolor(tup)
    tim.pendown()
    #only call pendown doesn't draw a circle. It needs to move point.
    tim.forward(2)
    tim.penup()

#moves point 50 from first circle from the previous line
def next_line(i):
    tim.setpos(0, 80*i+50)

tim.speed("fastest")
tim.penup()
tim.setpos(0, 50)

# Distance between circles vertically: 50
# Circle size: 30
# There must be a distance of at least 50 between the upper and lower boundaries.
# Subtract 50 to immediately fix the distances for the upper and lower borders.
for i in range(1, round((sc.window_height()-50)/80)+1):
    for j in range(1, int(sc.window_width()/50)-1):
        draw_circle()
    next_line(i)
print(sc.window_width(), sc.window_height())
sc.exitonclick()