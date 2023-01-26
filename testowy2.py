import math
def f(s):
    z = True
    x = len(s)
    for y in range(0, math.floor(x/2)-1):
        if s[y] == s[x-y-1]:
            z = True
        else:
            z = False
            break
    return z


print(f("12345432"))
