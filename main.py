import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = (screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                     "whats another states name?")).title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
