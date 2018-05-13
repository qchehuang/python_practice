# Implement a function to convert the ascii string to int.

import math

def atoi(str):

    len_str = len(str) -1

    value = 0

    for inter in str:
        print(inter)
        if inter not in ['0','1','2','3','4','5','6','7','8','9']:
            print("Invalid input for the literal for int()")
            return 'Invalid'

        value += int(inter) * int(math.pow(10,len_str))
        len_str = len_str - 1

    return value

if __name__ == "__main__":

    #last_value1 = atoi('123456')
    last_value2 = atoi('x12345')

    #print(last_value1)

    print(last_value2)