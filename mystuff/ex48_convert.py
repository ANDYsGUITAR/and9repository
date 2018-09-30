def convert_num(s):
    try:
        return int(s)
    except ValueError:
        return None

a = convert_num("520")
print(a)
b = convert_num("w")
print(b)
