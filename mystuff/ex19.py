# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print(f"You have {cheese_count} cheeses!")
#     print(f"You have {boxes_of_crackers} boxes of crackers!")
#     print("Man that's enough for a party!")
#     print("Get a blanket.\n")
#
#
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)
#
# print("Or, we can use variables from our script:")
# amount_of_cheeses = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheeses, amount_of_crackers)
#
# print("We can even do math inside too:")
# cheese_and_crackers(10+20, 5+6)
#
# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheeses+100,amount_of_crackers+1000)

def name_and_age(name, age):
    print(f"So your name is {name}, and you are {age} years old")

# 1
name_and_age("Andy", 22)

# 2
my_name = "Andy"
my_age = 22
name_and_age(my_name,my_age)

# 3
name_and_age("Andy",20+2)

# 4
name_and_age("Andy",my_age-2)

# 5
enter_name = input("Please enter your name: ")
enter_age = input("Please enter your age: ")
name_and_age(enter_name,enter_age)

# 6
name_and_age(enter_name,22)

# 7
name_and_age(enter_name,20+2)

# 8
name_and_age(enter_name,my_age+2-2)

# 9
name_and_age(enter_name+" WEI",my_age)

# 10
name_and_age(enter_name+" WEI",enter_age)
