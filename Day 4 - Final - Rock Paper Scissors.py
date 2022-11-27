import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


#scissors > paper
#paper > rock
#rock  > scissors

choice = input("What do you chooce? Type 0 for rock 1 for paper, 2 for scissors")
choice = int(choice)


gestures =[rock, paper , scissors]

print(gestures[choice])


computer_choice = random.randint(0,2)
computer_gesture = gestures[computer_choice]
print(computer_choice)
print(computer_gesture)

if computer_choice == choice:
  print("Even")

else:
  if choice ==0 and computer_choice ==2:
    print("winner")
  if choice ==0 and computer_choice ==1:
    print("loser")
  if choice == 1 and computer_choice == 0:
    print("winner")
  if choice == 1 and computer_choice ==2:
    print("loser")
  if choice == 2 and computer_choice == 1:
    print("win")
  if choice == 2 and computer_choice == 0:
    print("lose")


