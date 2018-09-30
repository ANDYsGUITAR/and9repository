def find_min_and_max(L):

    if L:
        min = L[0]
        max = L[-1]
        for x in L:
            if x < min:
                min = x
            if x > max:
                max = x
        return min, max
    else:
        return None, None


# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
