import random
import art

#Welcome

print(art.logo)

print("Welcome to Number Guessing Game\nChoose your skill level,")
print("I'm thinking number between 1 - 100.")
skill_level = input("Type 'easy' for easy and 'hard' for hard: ").lower()
if skill_level == "easy":
    attempts = 10
else:
    attempts = 5

the_number = random.randint(1,100)

should_continue = True

random.randint


while should_continue == True:
    
    guess = int(input(f"You have {attempts} attempts left, Please, Give a number: "))
    if guess == the_number:
        print("Correct, Nice Job!")
        should_continue = False
    elif guess > the_number:
        print("Too high")
    elif guess < the_number:
        print("Too low")
    attempts -= 1
    if attempts == 0:
        should_continue = False

    #ask for number
if attempts == 0:
    print("You lost the game!")

#print too high or too low
