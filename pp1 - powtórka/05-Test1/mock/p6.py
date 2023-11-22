def f(number, even):
    sum = 0
    for numb in str(number):
        if(int(numb)%2==0) == even:
            sum = sum + int(numb)
    return sum

print(f(3124,True))
f(3124,False)
f(20576,False)
f(20576,True)
f(13115,True)

        