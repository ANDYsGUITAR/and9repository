def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}\targ2: {arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}\targ2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing.")

print_two("Andy","WEI")
print_two_again("Andy","WEI")
print_one("YES")
print_none()
