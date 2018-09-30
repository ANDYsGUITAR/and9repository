def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def combinatorial_number(m, n):
    return int(factorial(n)/(factorial(m)*factorial(n-m)))


def triangles():
    n = 1
    yield [1]
    while n:
        L = [combinatorial_number(m, n) for m in range(0, n+1)]
        yield L
        n += 1


results = []
n = 0
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


# print(factorial(5))
# print(combinatorial_number(2, 4))
# triangles(5)