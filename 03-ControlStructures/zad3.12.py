a = str(input("Enter first person name: "))
b = int(input("Enter first person age: "))
c = str(input("Enter second person name: "))
d = int(input("Enter second person age: "))

if b>=18 and d>=18:
    print(f'Both {a} and {c} are adults')
elif b<18 and d>=18:
    print(f'{a} is not an adult')
elif b>=18 and d<18:
    print(f'{c} is not an adult')
else:
    print(f'Both {a} and {c} are not adults')