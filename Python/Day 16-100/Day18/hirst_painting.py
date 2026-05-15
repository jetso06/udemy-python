import turtle as t
import random
import colorgram


t.colormode(255)
tur = t.Turtle()

def coloring():
    colors = colorgram.extract('hirst_spotdrawing.jpg', 20)
    gram_color = []
    for c in range(0, 20):
        selected_color = colors[c]
        rgb = selected_color.rgb
        gram_color.append(rgb)
    gram_list = [(c.r, c.g, c.b) for c in gram_color]
    return gram_list


rgb_list = coloring()
for y in range(0, 500, 50):
    for x in range(0, 500, 510):
        tur.dot(20, random.choice(rgb_list))
        tur.teleport(x, y)


















my_screen = t.Screen()
my_screen.exitonclick()