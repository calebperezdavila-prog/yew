import turtle

def petal(t, radius, color1, color2):
    # Draw an outer circle
    t.color(color2)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Draw an inner circle
    t.color(color1)
    t.begin_fill()
    t.circle(radius * 0.7)
    t.end_fill()

def love(t, i):
    if i < 10:
        return
    t.color("green")
    t.forward(i)
    petal(t, 4, "yellow", "orange")

    t.left(30)
    love(t, 3 * i / 4)
    t.right(60)
    love(t, 3 * i / 4)
    t.left(30)

    t.color("green")
    t.backward(i)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Yellow Flower Day")

    flower = turtle.Turtle()
    flower.speed(0)
    flower.hideturtle()

    flower.left(90)
    flower.backward(60)
    love(flower, 60)

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, -250)

    message = "Anamaria, Happy Yellow Flower Day!!!"

    # Purple shadow
    writer.color("purple")
    writer.write(message, align="center", font=("Arial", 20, "bold"))

    # Pink overlay (slightly offset)
    writer.goto(0, -248)
    writer.color("pink")
    writer.write(message, align="center", font=("Arial", 20, "bold"))

    turtle.done()

if __name__ == "__main__":
    main()
