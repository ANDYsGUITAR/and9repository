import math


def quadratic(a, b, c):

    if a == 0:
        print("a shoule not be zero.")
        return None

    delta = b*b - 4*a*c
    if delta < 0:
        print("The equation has not real root.")
        return None
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1, x2


quadratic(0, 2 ,1)