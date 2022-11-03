import math
def f(x):
    s=0
    s=s+math.floor(x/5)
    x=x%5
    s=s+math.floor(x/2)
    x=x%2
    s=s+x
    return s

print(f(23))