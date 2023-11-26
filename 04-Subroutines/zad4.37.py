def f(n):
    a = 1
    b = 1
    c = 0
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 1
    else:
        for x in range(n-3,0,-1):
            c = a + b
            a = b
            b = c
    return c

print(f(9))