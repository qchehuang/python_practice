def divided_by_3_5(input_num):
    value = 0
    for i in range(0, input_num):
        if i % 3 == 0 or i % 5 == 0:
            value +=  i
            print(i)
    return value


if __name__ == "__main__":
    value = divided_by_3_5(1000)
    print("value = ", value)