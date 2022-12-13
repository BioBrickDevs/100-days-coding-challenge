
index = []

for x in range(1, 6):
    index.append([data for data in range(1,6)])

lenght = 4

def horizontal(index):
    result = []
    global lenght
    y = 0
    x = 0
    len_hor = len(index[1])
    len_ver = len(index)
    while y <= len_ver-1:
        while x + lenght <= len_hor:
            temp = []
            for i in range(x, x + lenght):
                temp.append(index[y][i])
            result.append(temp)
            x += 1
        y += 1
        x = 0

    return result




def vertical(index):
    result = []
    global lenght
    x = 0
    y = 0
    len_hor = len(index[1])
    len_ver = len(index)
    while x <= len_ver-1:
        while y + lenght <= len_hor:
            temp = []
            for i in range(y, y + lenght):
                temp.append(index[i][x])
            result.append(temp)
            y += 1
        x += 1
        y = 0

    return result

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5


def diagonal_up(index):
    result = []
    global lenght
    temp_list = []
    lenght_for_this = lenght -1
    x = 0
    y = 0
    len_hor = len(index[1])
    len_ver = len(index)
    while x <= len_ver-1:
        while y < len(index):
            if y - lenght_for_this >= 0 and x + lenght_for_this < len_hor:
                print(y,x)
                #print(lenght-x)
                tempy = y
                tempx = x
                temp_list = []
                while tempy > -1 and tempx < len_ver:
                    print(index[tempy][tempx])
                    temp_list.append(index[tempy][tempx])
                    tempy -= 1
                    tempx += 1
                    
                result.append(temp_list)
                print("---------------------")            
            y+=1
        y = 0
        x += 1
            

    result_temp = []

    for row in result:
        start_index = 0
        last_index = len(row)-1
        temp_list = []
        while start_index + lenght<= len(row):
            temp_list.append(row[start_index: start_index+lenght])    
            start_index +=1
        result_temp.append(temp_list)    
        #print(row)

        print("----------------")
    result = []
    for row in result_temp:
        print(row)
        print("-----------------------up")
        for row in row:
            print("------------------down")
            print(row)
            result.append(row)

    return result       
            

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5



            
def diagonal_down(index):
    result = []
    global lenght
    temp_list = []
    lenght_for_this = lenght -1
    x = 0
    y = 0
    len_hor = len(index[1])
    len_ver = len(index)
    while x <= len_ver-1:
        while y < len(index):
            if x + lenght < len_hor:
                print(x)
                #print(lenght-x)
                tempy = y
                tempx = x
                temp_list = []
                while tempy < len_ver and tempx <6:
                    print(index[tempy][tempx])
                    temp_list.append(index[tempy][tempx])
                    tempy += 1
                    tempx += 1
                    
                result.append(temp_list)
                print("---------------------")            
            y+=1
        x += 1
            

    result_temp = []

    for row in result:
        start_index = 0
        last_index = len(row)-1
        temp_list = []
        while start_index + lenght<= len(row):
            temp_list.append(row[start_index: start_index+lenght])    
            start_index +=1
        result_temp.append(temp_list)    
        #print(row)

        print("----------------")
    result = []
    for row in result_temp:
        print(row)
        print("-----------------------up")
        for row in row:
            print("------------------down")
            print(row)
            result.append(row)

    return result

            
print(diagonal_down(index))






