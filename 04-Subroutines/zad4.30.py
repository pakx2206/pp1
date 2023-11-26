def f(number,even):
    sum = 0
    y = str(number)
    for x in range(len(y)):
        if even==True:
            if int(y[x])%2==0:
                sum+=int(y[x])
        else:
            if int(y[x])%2==1:
                sum+=int(y[x])
    return sum

print(f(13115,True) )

        