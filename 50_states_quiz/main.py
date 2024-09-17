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

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
correct_guesses = 0
guess_list = []

still_guessing = True
while still_guessing:
    formatted_answer_state = answer_state.title()
    if len(guess_list) < 49:
        if formatted_answer_state in state_list:
            correct_guesses += 1
            guess_list.append(formatted_answer_state)
            correct_guess = data[data.state == formatted_answer_state]
            x_coord = int(correct_guess['x'].iloc[0])
            y_coord = int(correct_guess['y'].iloc[0])
            new_turtle.teleport(x_coord, y_coord)
            new_turtle.write(formatted_answer_state)
            answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                            prompt="What's another state's name?")
        else:
            answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                            prompt="What's another state's name?")
    else:
        new_turtle.teleport(250, 0)
        new_turtle.write(f"Congrats!\n You guessed all 50 States!", align='center',
                         font=('Courier', 24, 'normal'))

turtle.mainloop()
