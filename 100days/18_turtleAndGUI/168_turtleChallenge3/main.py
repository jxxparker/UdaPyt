import turtle as t 
from turtle import Screen

tim = t.Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
# draw_shape()
for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen = Screen() #doesn't let screen exit, because without it it does.
screen.exitonclick() 

