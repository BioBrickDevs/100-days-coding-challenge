#add
def add(n1, n2):
    return n1 + n2

#subscratct 
def substract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2

methods = {
"+": add,
 "-": substract,
"*" : multiply,
 "/": divide,
 
 }

num1 = int(input("Give first number: "))

for operation in methods:
    print(operation)




operation = input ("Give operation: ")

num2 = int(input("Give second number: "))

fuction = methods[operation]
answer = fuction(num1, num2)
print(f"The answer is: {num1} {operation} {num1} = {answer}")
continue_calculation = True
while continue_calculation == True:
    yes_no = input(f'continue calculating with {answer}? "y" /"n" :')
    if yes_no == "n":
        continue_calculation = False
    else:
        operation = input ("Give operation: ")
        num2 = int(input("Give second number: "))
        answer = fuction(answer, num2)
        print(f"The answer is: {answer} {operation} {num2} = {answer}")
       
