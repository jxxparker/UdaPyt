import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/jihunpark/Desktop/UdaPyt/100days/25_csvData/230_cvsGame/states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('/Users/jihunpark/Desktop/UdaPyt/100days/25_csvData/231_csvGame2/50_states.csv')
all_states = data.state.to_list() #to_list turns data.state into a list
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()

    

    #if answer_state is one of the states in all the states of the 50+states.csv
        #if they got it right:
            #create a turtle to write the name of the state at the state's x and y coordinate
    if answer_state in all_states:
        guessed_states.append(answer_state) 
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick() 