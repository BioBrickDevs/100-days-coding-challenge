import turtle
import pandas
import answer




score_board = answer.Answer()


screen = turtle.Screen()

image = "blank_states_img.gif"


screen.register_shape(image)

turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
score = 0
correct_answers = []
list_of_states = states_data["state"].to_list()
guess = 0
while True:
    try:
        guess = screen.textinput("Not Shown" ,f"Correct {score} / 50 ", ).title()
        if guess == "Exit":
            break
    except:
        pass
    
    if not guess:
        break
    try:
        data_for_state = states_data[states_data["state"]==guess]
        if data_for_state.empty:
            pass
            
        else:
            if guess not in correct_answers:
                correct_answers.append(guess)
                score += 1
                score_board.right(x=int(data_for_state.x.values[0]), y=int(data_for_state.y.values[0]), state_name=data_for_state.state.values[0])
    except:
        pass
    print("tomii")

a = set(correct_answers)
b = set(list_of_states)

c = b.difference(a)
print("Toimii")
print(c)
print(len(c))

c_data = pandas.DataFrame(c)

c_data.to_csv("file.csv")