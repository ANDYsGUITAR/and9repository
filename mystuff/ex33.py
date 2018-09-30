# def loops_f(x,y):
#
#     i = 0
#     numbers = []
#
#     while i < x:
#         print(f"At the top i is {i}")
#         numbers.append(i)
#
#         i += y
#         print("Numbers now: ",numbers)
#         print(f"At the bottom i is {i}")
#
#     print("The number: ")
#
#     for num in numbers:
#         print(num)
#
# loops_f(10,2)
numbers = []
for i in range(0,10):
    numbers.append(i)

for num in numbers:
    print(num)
