import turtle as t 
from turtle import Screen

tim = t.Turtle()


for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()     

screen = Screen() #doesn't let screen exit, because without it it does.
screen.exitonclick() 