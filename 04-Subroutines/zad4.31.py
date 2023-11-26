def f(x,y):
    sum = 0
    for z in range(x, 0):
        if z%2==0:
            sum+=1
    return sum
print(f(-1,11) )