from numpy import *
import time

def random_initialize(demen):

    matrix_list = []
    bin_value_list = []

    data1 = mat(zeros((demen, demen)))

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

if __name__ == "__main__":

    demen = 2
    my_matrix_list = random_initialize(demen)

    my_swap_row_list = []

    for i in my_matrix_list:
        #print(i)
        for j in range(0, demen):
            i[[j,demen-1], :] = i[[demen-1,j],:]
            my_swap_row_list.append(i)

            for n in my_swap_row_list:
                print(n)

        time.sleep(10)
    my_swap_row_list.clear()

