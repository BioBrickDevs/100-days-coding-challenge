def Collatz_generator(n):
    
    while n != 1:
       
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3* n + 1 
        yield n
 
    


def main():
    index = 1000000
    max = 0
    while index > 0:
        my = Collatz_generator(index)
        lenght = len(list(my))
        if lenght > max:
            print(lenght)
            max = lenght
            print(index)
        
        
        index -= 1
        
        
main()