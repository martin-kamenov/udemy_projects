import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_answers = []

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

while len(correct_answers) < len(all_states):

    state_answer = screen.textinput(f"{len(correct_answers)}/{len(all_states)} States Correct",
                                    "What's another state name?").title()

    if state_answer == "Exit":
        missing_states = [state for state in all_states if state not in correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if state_answer in all_states:
        correct_answers.append(state_answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state = states_data[states_data.state == state_answer]
        t.goto(state.x.item(), state.y.item())
        t.write(state_answer)