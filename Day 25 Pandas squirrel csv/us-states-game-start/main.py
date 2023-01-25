import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#
# Gets Mouse coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
# print(states)

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another State name").title()

    # read data from csv
    for state in states:
        if state == answer:
            guessed_states.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            # t.write(state_data.state.item())
            t.write(answer)

    if answer == "Exit":
        missing_states = []
        for state in states:
            missing_states = [state for state in states if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("States to learn.csv")

        break


# Keeps screen open
# turtle.mainloop()


screen.exitonclick()