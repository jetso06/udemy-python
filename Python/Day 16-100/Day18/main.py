import turtle as t
import random
import colorgram

timm = t.Turtle()
t.shape("arrow")
t.speed("fastest")
#t.width(10)

t.colormode(255)

#colour = ["blue", "red", "green", "violet", "brown", "medium sea green", "dark green", "orange red", "deep pink", "indigo"]
#direction = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for p in range(0, 360, 5):
    t.color(random_color())
    t.setheading(p)
    t.circle(100)



# for walk in range(200):
#     selected_color = random_color()
#     timm.pencolor(selected_color)
#     timm.setheading(random.choice(direction))
#     timm.forward(30)



# for s in range(3, 11):
#     angle = 360/s
#     timm.color(random.choice(colour))
#     for draw in range(s):
#         timm.forward(100)
#         timm.left(angle)












my_screen = t.Screen()
my_screen.exitonclick()

