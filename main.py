import random
import turtle
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race: red, orange, yellow, green, blue, purple? Type a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x=-240
y=-130
index = colors.index(user_bet)
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 50
    new_turtle.color(colors[index - 5])
    index += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You're won! The {winning_color} turtle is winner!")
            else:
                print(f"You're lost! The {winning_color} turtle is winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
