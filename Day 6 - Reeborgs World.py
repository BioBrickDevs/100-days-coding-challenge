#Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()
 

while not at_goal():
    
    if wall_in_front() == True:
        if right_is_clear():
            turn_right()
            move()
        else:
             turn_left()
             
    elif right_is_clear() and wall_in_front():
       turn_right()
       move()
       turn_right()
       move()     
    else:
        move()