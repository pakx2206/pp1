def f(amount_to_pay):
    sum = 0
    x = amount_to_pay
    sum+=int(x/5)
    x = x%5
    sum +=int(x/2)
    x = x%2
    sum +=int(x)
    return sum
print(f(23))