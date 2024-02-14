import turtle

valent = turtle.Screen()
valent.bgcolor("black")

def draw_heart():
    t = turtle.Turtle()
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    t.hideturtle()

def write_message(message):
    t = turtle.Turtle()
    t.penup()
    t.color("white")
    t.goto(-120, -50)
    t.write(message, font=("Arial", 20, "normal"))
    t.hideturtle()
draw_heart()

write_message("Happy Valentine's Day")

for _ in range(5):
    valent.bgcolor("black")
    valent.delay(100)
    valent.bgcolor("red")
    valent.delay(100)

valent.mainloop()
