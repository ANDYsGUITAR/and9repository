def product(a,*numbers):
    m = a
    for x in numbers:
        m *= x

    return m


print(product(1, 2, 3))
print(product(1))

