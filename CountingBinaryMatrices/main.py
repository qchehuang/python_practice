from numpy import *
import time

def matrix_initialize(demen):

    matrix_list = []
    bin_value_list = []

    value = pow(2, demen*demen)

    for i in range(0, value):
        bin_value = bin(i)[2:].zfill(demen * demen)

        bin_value_list.clear()
        for x in bin_value:
            bin_value_list.append(x)

        my_ndarray = array(bin_value_list)
        my_ndarray = my_ndarray.reshape(demen,demen)

        matrix_list.append(my_ndarray)

    return matrix_list

def convert_row(array, x, y):
    temp = array.copy()
    temp[[x,y],:] = temp[[y,x],:]
    return temp

def clean_swap_order_list(list):
    x = 0
    for i in list:
        x = x + 1
        a, b = i[0],i[1]
        a, b = b, a
        for j in list[x:]:
            if j == [a, b]:
                #print(j)
                list.remove(j)
    return


if __name__ == "__main__":

    #a = array([0,1,2,4,5,6,7,8,9])
    #a = a.reshape(3,3)

    #for i in range(0,3):
        #t = row_swap_list[i]

        #print(a)
        #b = convert_row(a, row_swap_list[i][0], row_swap_list[i][1])

        #print(t[0], " ", t[1])
        #print(b)
        #print("==============================")


    demen = 3

    my_matrix_list = matrix_initialize(demen)

    row_swap_order_list = []
    matrix_record_list  = []
    for i in range(0, demen):
        for j in range(0, demen):
            if i is not j:
                row_swap_order_list.append([i, j])

    clean_swap_order_list(row_swap_order_list)

    for i in my_matrix_list:
        for j in range(0, len(row_swap_order_list)):
            print(row_swap_order_list)
            print("=======")
            print(i)
            print("==============")
            a = convert_row(i, row_swap_order_list[j][0], row_swap_order_list[j][1])
            print(a)
            print("=======")
            print('\n\n')
            matrix_record_list.append(a)

