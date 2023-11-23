i = 2
for x in range(1,10):
    if x<=5:
        print('*'*x)
    else:
        x-=i
        i+=2
        print('*'*x)