# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined = 0
combined2 = 0
name1 = name1.lower()
name2 = name2.lower()
name1 += name2

combined += name1.count("l")
combined += name1.count("o")
combined += name1.count("v")
combined += name1.count("e")

combined2 += name1.count("t")
combined2 += name1.count("r")
combined2+= name1.count("u")
combined2 += name1.count("e")

score = str(combined2) + str(combined)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

