a = 0
b = 1
c = 0
for x in range(0,20,1):
    if x==0:
        print("0", end=' ')
    elif x==1:
        print("1",end=' ')
    else:
        c = a+b
        a=b
        b=c
        print(c,end=' ')