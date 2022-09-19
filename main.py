import turtle
import pandas

image = "blank_states_img.gif"
guess_states = []


def create_state_text(name_of_state, x_pos, y_pos):
    state_name_text = turtle.Turtle()
    state_name_text.speed("fastest")
    state_name_text.hideturtle()
    state_name_text.penup()
    state_name_text.goto(x=x_pos, y=y_pos)
    state_name_text.write(f"{name_of_state}")


state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
learn_state_list = []

screen = turtle.Screen()
screen.title("US State Guessing Game")
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

while len(guess_states) < 50:
    new_answer_state = turtle.textinput(title=f"{len(guess_states)}/50 Correct Guessed", prompt=f"Enter States name here")
    new_answer_state = new_answer_state.capitalize()
    if new_answer_state in state_list:
        state = state_data[state_data["state"] == new_answer_state]
        x = int(state.x)
        y = int(state.y)
        create_state_text(name_of_state=new_answer_state, x_pos=x, y_pos=y)
        guess_states.append(new_answer_state)
    elif new_answer_state == "Exit":
        for state_name in state_list:
            if state_name not in guess_states:
                learn_state_list.append(state_name)
        learn_state = pandas.DataFrame(learn_state_list)
        learn_state.to_csv("state_to_learn.csv")
        break

turtle.mainloop()
