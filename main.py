import turtle
from turtle import Turtle,Screen
#from the turtle import the turtle class and screen class
import random
is_game_on = False
#this imports the random module
screen = Screen()
colors = ["green","yellow","blue","orange","purple","red"]
y_positions = [-70,-50,-10,20,50,70]
# these are the y coordinates of the turtles x remains constant with a value of -210
user_bet = screen.textinput(title="winner",prompt="Who is going to win the race")
#This line of code brings up a popup that allows the user to enter the turtle color that they expect to win
screen.setup(width=500,height=400)
all_turtles = []
#this creates 6 turtles with 6 different colors
for turtle_index in range(0,6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.penup()
    new_turtles.goto(x=-210, y=y_positions[turtle_index])
    new_turtles.color(colors[turtle_index])
    all_turtles.append(new_turtles)

if user_bet:
    #if user has put a bet the is_game_on booolean becomes true
    is_game_on = True
while is_game_on:
    for turtle in all_turtles:
        if is_game_on:
          if turtle.xcor() > 210:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The turtle that won is {winning_color}. You won!")
            else:
                print(f"The turtle that won is {winning_color}. You lost")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
