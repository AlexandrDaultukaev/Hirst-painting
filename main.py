
import turtle as t
import random
import colorgram

t.colormode(255)
tim = t.Turtle()
colors = colorgram.extract("hirst_art/HirstArt.jpg", 15)
tim.pensize(30)


def draw_circle():
    rand_choice = random.choice(colors)
    tup = (rand_choice.rgb[0], rand_choice.rgb[1], rand_choice.rgb[2])
    tim.penup()
    tim.forward(50)
    tim.pencolor(tup)
    tim.pendown()
    tim.forward(1)


for _ in range(10):
    draw_circle()


sc = t.Screen()
sc.exitonclick()