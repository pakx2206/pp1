def f(binary_number):
    for x in range(0,len(binary_number)):
        if binary_number[x]!="0" and binary_number[x]!="1":
            return False
    return True

print(f("101101"))
print(f("1311a10100"))