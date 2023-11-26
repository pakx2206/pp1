def f(number1,number2,number3):
    arr = [number1,number2,number3]
    arr.sort()
    return arr[2]-arr[0]

print(f(2,12,8))