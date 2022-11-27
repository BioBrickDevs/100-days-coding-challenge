# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap_year = False

if year % 4  == 0:
    leap_year = True
    
    if year % 100 ==0:

        if year % 400  ==0:
            leap_year = True
        else:
            leap_year = False

if leap_year:
    print("Leap year.")
else:
    print("Not leap year.")
    
    
