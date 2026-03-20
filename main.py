from turtle import *
from random import randrange


class vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def copy(self):
        return vector(self.x, self.y)

    def move(self, other):
        self.x += other.x
        self.y += other.y

    def __eq__(self, other):
        return isinstance(other, vector) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"vector({self.x}, {self.y})"


def square(x, y, size, color):
    """Draw a filled square centered at (x, y) using the turtle module."""
    penup()
    goto(x - size / 2, y - size / 2)
    pendown()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()
    penup()


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Movement delay (milliseconds). Lower value = faster snake.
DELAY = 100


def change(x, y):
    """Change direction of snake's head movement."""
    global aim
    aim.x = x
    aim.y = y


def change_speed(delta):
    """Increase/decrease the movement delay to change game speed."""
    global DELAY
    # delta is added to DELAY; negative delta makes game faster
    DELAY = max(10, DELAY + delta)
    print(f"Speed delay set to {DELAY} ms (lower is faster)")


def inside(head):
    """Return True if head inside the playing area."""
    return -200 < head.x < 200 and -200 < head.y < 200


def move():
    """Advance the snake by one step and schedule the next move."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    # schedule next move using current DELAY
    ontimer(move, DELAY)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Speed controls: press 'z' to speed up, 'x' to slow down
onkey(lambda: change_speed(-10), 'z')
onkey(lambda: change_speed(10), 'x')

move()
done()









# import math
# from turtle import*
# def hearta(k):
#     return 15*math.sin(k)*3
# def heartb(k):
#     return 12*math.cos (k)-5*\
#            math.cos(2*k)-2*\
#            math.cos(3*k)-\
#            math.cos(4*k)
# speed (1000)
# bgcolor("black")
# for i in range(6000):
#     goto(hearta(i)*20,heartb(i)*20)
#     for j in range(5):
#         color("#f73434")
#     goto(0,0)
# done    





# import turtle
# her = turtle.Turtle()
# her.speed(10)
# turtle.title("Heart Shape")
# screen = turtle.Screen()
# screen.bgcolor("black")
# her.color("pink")
# her.begin_fill()
# her.fillcolor("red")
# her.left(140)
# her.forward(180)
# her.circle(-90,200)
# her.setheading(60)
# her.circle(-90,200)
# her.forward(180)
# her.end_fill()




# import turtle as t
# import colorsys

# t.bgcolor("black")
# t.tracer(100)
# t.pensize(1)
# h = 0.5

# for i in range(250):
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     h += 0.0008
#     t.fillcolor(c)
#     t.begin_fill()
#     t.fd(i)
#     t.lt(100)
#     t.circle(30)
#     for j in range(2):
#         t.fd(i * j)
#         t.rt(109)
#     t.end_fill()




# import turtle as t
# import colorsys

# t.bgcolor("black")
# t.speed(0)
# t.pensize(2)
# h = 0.0

# for i in range(36):
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     h += 0.028
#     rgb = tuple(int(x * 255) for x in c)
#     hex_color = '#%02x%02x%02x' % rgb
#     t.pencolor(hex_color)
#     t.fillcolor(hex_color)
#     t.begin_fill()
#     for j in range(6):
#         t.forward(100)
#         t.left(60)
#     t.end_fill()
#     t.right(10)

# t.hideturtle()
# t.done()




# import turtle as t
# import colorsys

# #Setup turtle
# t.bgcolor("silver")
# t.tracer(0)
# t.pensize(1)
# t.speed(0)
# t.colormode(255)  # use 0-255 RGB values

# # Draw "colorful" pattern
# h = 0.5
# for i in range(250):
#     # colorsys provides values in 0..1 — convert to 0..255
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     h += 0.0008
#     rgb = tuple(int(x * 255) for x in c)
#     hex_color = '#%02x%02x%02x' % rgb

#     t.fillcolor(hex_color)
#     t.begin_fill()
#     t.fd(i)
#     t.lt(100)
#     t.circle(30)
#     for k in range(2):
#         t.fd(i * k)
#         t.rt(109)
#     t.end_fill()

# t.hideturtle()
# t.done()






