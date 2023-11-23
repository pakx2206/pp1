import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
p = (a+b+c)/2
print(f'Triangle area: {math.sqrt(p*(p-a)*(p-b)*(p-c))}')
print(f'Triangle circumference: {a+b+c}')