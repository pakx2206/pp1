def f(binary_number):
    for bi in binary_number:
        if bi!="1" and bi!="0":
            return False
    return True
        
print(f("1311a10100"))
print(f("10101011"))


