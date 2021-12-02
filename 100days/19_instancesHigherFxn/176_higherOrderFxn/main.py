from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)

screen = Screen()
screen.listen()
screen.exitonclick()
screen.onkey(key="space" ,fun=move_forwards)

