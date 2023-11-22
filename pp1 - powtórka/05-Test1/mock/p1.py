def f(amount_to_pay):
    x = amount_to_pay
    mod = int(x/5)
    x = x-5*mod
    sum = mod
    mod = int(x/2)
    sum = sum + mod
    x = x-2*mod
    sum = sum + x
    return sum

print(f(23))

