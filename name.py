import turtle




screen = turtle.Screen()


screen.setup(800, 800)


screen.bgcolor('pink')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)
t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()



t.goto(150,150)
a = t.stamp()
t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("Georgia", 30, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Abby Conlan", font=("Georgia", 30, "bold"), align="center")
enter = input("press enter to begin")
t.showturtle()
t.clear()
screen.bgcolor('purple')


t.penup()
t.goto(0,250)
t.write("My favorite food", font=("Georgia", 30, "bold"), align="center")


turtle.addshape("pizza.gif")
t.shape("pizza.gif")
t.goto(150,150)
a = t.stamp()
t.hideturtle()
t.goto(150,200)
t.write("Pizza", font=("Georgia", 30, "bold"), align="center")


turtle.addshape("macandcheese.png")
t.shape("macandcheese.png")
t.goto(0,0)
b = t.stamp()
t.goto(0,50)
t.write("mac and cheese", font=("Georgia", 30, "bold"), align="center")
turtle.addshape("strawberry.png")
t.shape("strawberry.png")
t.goto(-150,-150)
c = t.stamp()
t.goto(0,0)
t.goto(-150,-100)
t.write("strawberry.png", font=("Georgia", 30, "bold"), align="center")
enter = input("press enter to begin")
t.clear()
t.clearstamps()
screen.bgcolor('purple')
t.penup()
t.goto(0,200)
t.write("My favorite hobbies", font=("Georgia", 30, "bold"), align="center")


t.goto(150,50)
t.write("Gymnastics", font=("Georgia", 30, "bold"), align="center")
turtle.addshape("gymnastics.gif")
t.shape("gymnastics.gif")
t.goto(150,150)
d = t.stamp()
t.hideturtle()


t.goto(0,-100)
t.write("Taking walks", font=("Georgia", 30, "bold"), align="center")
turtle.addshape("walking.gif")
t.shape("walking.gif")
t.goto(0,0)
e = t.stamp()


t.goto(150,-250)
t.write("Shopping", font=("Georgia", 30, "bold"), align="center")
turtle.addshape("shopping.gif")
t.shape("shopping.gif")
t.goto(150,-150)
f = t.stamp()
t.goto(0,0)


t.goto(-150,50)
t.write("baking", font=("Georgia", 30, "bold"), align="center")
turtle.addshape("baking.gif")
t.shape("baking.gif")
t.goto(-150,150)
g = t.stamp()
t.goto(0,0)
t.penup()
t.goto(-150,-200)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.setheading(45)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.end_fill()


enter = input("press enter to continue")
t.clear()
t.clearstamps()


turtle.done()





