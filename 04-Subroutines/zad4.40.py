def f(number):
    it=0
    sum=0
    number = str(number)
    for x in range(0,10,1):
        it=0
        for y in range(0, len(number)):
            if int(number[y])==x:
                it+=1
        if it>1:
            sum+=x*it
    return sum

print(f(230335))
