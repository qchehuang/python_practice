# Implement a function to convert the ascii string to int.

import math

def atoi(str):

    len_str = len(str) -1
    value = 0
    negative = False

    for inter in str:
        if inter is '-':
            len_str = len_str - 1
            negative = True
            continue
        else:
            if inter not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("invalid input for the literal for int")
                return 'invalid'
            else:
                value += int(inter)*int(math.pow(10,len_str))
                len_str = len_str - 1

    if negative is True:
        return -1 * value
    else:
        return value


if __name__ == "__main__":

    return_value1 = atoi('123456')
    return_value2 = atoi('x12345')
    return_value3 = atoi('1xx345')
    return_value4 = atoi('-12345')

    print("value1 = ", return_value1)
    print("value2 = ", return_value2)
    print("value3 = ", return_value3)
    print("value4 = ", return_value4)