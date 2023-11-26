import math
def f(number1, number2, operator):
    if operator=="+":
        return number1+number2
    elif operator=="%":
        return number1%number2
    elif operator=="**":
        return int(math.pow(number1,number2))
    elif operator=="*":
        return number1*number2
    elif operator=="-":
        return number1-number2
    
print(f(2, 3, "+"))   # Output: 5
print(f(2, 3, "%"))   # Output: 2
print(f(2, 3, "**"))  # Output: 8
print(f(2, 3, "*"))   # Output: 6
print(f(2, 3, "-"))