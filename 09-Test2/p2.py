def f(human_age):
    n = human_age
    sum=0
    while n>0:
        if n>2:
            sum+=4
            n-=1
        else:
            sum+=10
            n-=1
    return sum

print(f(2))