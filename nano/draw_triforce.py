import turtle ##animations/drawing


def triforce():
    din = turtle.Turtle()
    din.color('pink')
    din.setx(-250)
    din.sety(-250)
    din.shape("turtle")
    din.color("purple")
    din.speed(30)
    for i in range(1, 4):
        din.forward(500)
        din.left(120)
    for i in range(1, 5):
        din.forward(250)
        din.left(120)
    for i in range(1, 5):
        din.forward(250)
        din.right(120)
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("pink")
    triforce()
    window.exitonclick()
draw_shapes()
