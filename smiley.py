import turtle

def draw_smiley():
    p=turtle.Turtle()
    p.speed(0)
    screen=turtle.Screen()
    screen.bgcolor("white")

    def draw_eye(col,rad):
        p.down()
        p.fillcolor(col)
        p.begin_fill()
        p.circle(rad)
        p.end_fill()
        p.up()

    p.fillcolor('yellow')
    p.begin_fill()
    p.circle(100)
    p.end_fill()
    p.up()

    p.goto(-40,120)
    draw_eye('white',15)
    p.goto(-37,125)
    draw_eye('black',5)
    p.goto(40,120)
    draw_eye('white',15)
    p.goto(40,120)
    draw_eye('black',5)

    p.goto(-40,85)
    p.down()
    p.right(90)
    p.circle(40,180)
    p.up()

    p.goto(-10,45)
    p.down()
    p.right(180)
    p.fillcolor('red')
    p.begin_fill()
    p.circle(10,180)
    p.end_fill()
    p.hideturtle()
    turtle.done()

draw_smiley()
