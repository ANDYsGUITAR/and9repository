def sum_from_1_to(x):
    sum = 0
    for i in range(1, x+1):
        sum += i

    return sum

n = int(input("Please enter an integer: "))
print("The result is {}".format(sum_from_1_to(n)))
