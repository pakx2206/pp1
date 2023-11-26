def f(x,y):
    sum = 0
    for z in range(x, y+1):
        if z%2==0:
            if z%3==0:
                if z%4!=0:
                    sum+=z
    return sum

print(f(10,30) )