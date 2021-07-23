import turtle as t
import random
# for extract colors from an image
import colorgram

sc = t.Screen()
t.colormode(255)
tim = t.Turtle()
t.setworldcoordinates(0, 0, sc.window_width(), sc.window_height())
tim.pensize(30)
rgb_colors = [(1, 12, 31), (53, 25, 17), (218, 127, 106),
               (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102),
              (10, 64, 33)]


# move forward and draw one circle
def draw_circle():
    tup = (random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)
    tim.pencolor(tup)
    tim.pendown()
    # only call pendown doesn't draw a circle. It needs to move point.
    tim.forward(2)
    tim.penup()


# moves point 50 from first circle from the previous line
def next_line(i):
    tim.setpos(0, 80 * i + 50)


tim.speed("fastest")
tim.penup()
tim.setpos(0, 50)

# Distance between circles vertically: 50
# Circle size: 30
# There must be a distance of at least 50 between the upper and lower boundaries.
# Subtract 50 to immediately fix the distances for the upper and lower borders.
for i in range(1, round((sc.window_height() - 50) / 80) + 1):
    for j in range(1, int(sc.window_width() / 50) - 1):
        draw_circle()
    next_line(i)
print(sc.window_width(), sc.window_height())
sc.exitonclick()
