from turtle import Turtle, Screen

import pandas

import time

from state import State

prompt = Screen()
prompt.title("U.S. States Game")
prompt.bgpic("blank_states_img.gif")
prompt.bgcolor("beige")

states_said = []

tally = 0

new_input = str(prompt.textinput(f"{tally}/ 50 States Guessed!", "State: "))

data = pandas.read_csv("50_states.csv")


game_is_on = True

while game_is_on:

    prompt.update()
    time.sleep(0.1)

    if new_input == "Exit":
        new_list = [state for state in data["state"] if state not in states_said]
        study_dict = {

            "States": new_list

        }

        study_df = pandas.DataFrame.from_dict(study_dict)
        study_df.to_csv("states_to_study.csv")
        game_is_on = False


    if new_input == None:
        new_input = prompt.textinput(f"{tally}/ 50 States Guessed!", "State: ")
    elif new_input not in data.values:
        new_input = prompt.textinput(f"{tally}/ 50 States Guessed!", "State: ")
    else:
        state_guess = new_input

    if state_guess in data.values and state_guess not in states_said:
        states_said.append(state_guess)
        tally += 1
        print(tally)

        x_arg_row = data[data["state"] == state_guess]
        x_arg = x_arg_row["x"].values[0]
        y_arg = x_arg_row["y"].values[0]
        print(x_arg)
        print(y_arg)

        new_state = State(user_input=state_guess, x_input=x_arg, y_input=y_arg)
        new_input = prompt.textinput(f"{tally}/ 50 States Guessed!", "State: ")

    if tally == 50:
        break
