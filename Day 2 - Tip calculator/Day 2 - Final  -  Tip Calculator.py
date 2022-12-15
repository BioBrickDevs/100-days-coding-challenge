print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
persons = input("Whow many people to split the bill? ")

bill = float(bill)
tip_percent = float(tip_percent) / 100 + 1
persons = int(persons)

sum_per_person = round((bill * tip_percent) / persons, 2)

sum_per_person = "{:.2f}".format(sum_per_person)


print(f"Each person should pay: ${sum_per_person}")