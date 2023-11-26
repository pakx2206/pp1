def f(product_code):
    sum = int(product_code[0])+int(product_code[1])+int(product_code[2])
    return sum%7==int(product_code[3])

print(f("1083"))