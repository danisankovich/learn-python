import turtle ##animations/drawing
## the class of Turtle
##brad angie, and zack are instances of the Turtle class
def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color('yellow')
    brad.speed(2)
    count = 0
    while(count < 4):
        brad.forward(100) ##right 100 pixels
        brad.right(90) ##right 90 degrees
        count += 1
def draw_circle():
    angie = turtle.Turtle() ##another instance of the Turtle class
    angie.shape("arrow")
    angie.color("purple")
    angie.circle(100)

def draw_triangle():
    count = 0
    zack = turtle.Turtle()
    zack.shape("classic")
    zack.color("black")
    zack.speed("5")
    while(count < 3):
        zack.forward(100)
        zack.right(120)
        count +=1
    

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()
#draw_shapes()

def circle_square():
    count = 0
    loop = 0
    cub = turtle.Turtle()
    cub.shape("turtle")
    cub.color("purple")
    cub.speed(30)
    while(loop < 72):
        if(count != 0):
            count = 0
        while(count < 4):
            cub.forward(100)
            cub.right(90)
            count += 1
        cub.right(5)
        loop += 1
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("pink")
    circle_square()
    window.exitonclick()
draw_shapes()

