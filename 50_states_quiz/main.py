import turtle
import pandas


data = pandas.read_csv("50_states.csv")
state_list = data['state'].to_list()

screen = turtle.Screen()
screen.title("50 States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
new_turtle = turtle.Turtle()
new_turtle.ht()

guess_list = []

while len(guess_list) < 50:
    answer_state = screen.textinput(title=f"{len(guess_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = []
        for state in state_list:
            if state not in guess_list:
                missed_states.append(state)
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv('states_to_learn.csv')
        break
    if answer_state in state_list:
        guess_list.append(answer_state)
        correct_guess = data[data.state == answer_state]
        x_coord = int(correct_guess['x'].iloc[0])
        y_coord = int(correct_guess['y'].iloc[0])
        new_turtle.teleport(x_coord, y_coord)
        new_turtle.write(answer_state)






# new_turtle.teleport(250, 0)
# new_turtle.write(f"Congrats!\n You guessed all 50 States!", align='center',
#                  font=('Courier', 24, 'normal'))

