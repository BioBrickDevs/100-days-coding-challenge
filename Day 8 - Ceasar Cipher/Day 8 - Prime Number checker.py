#Write your code below this line 👇
import math

def prime_checker(number):
    value = number
    list_of_candidates = []
    list_of_candidates.extend(range(2,value+1))
    list_of_primes = []
    value = list_of_candidates[0]
    while list_of_candidates:
        value = list_of_candidates[0]
        for index in list_of_candidates:
            if index % value == 0:
                list_of_candidates.remove(index)
        list_of_primes.append(value)

    
#Write your code above this line 👆
    if number in list_of_primes:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)