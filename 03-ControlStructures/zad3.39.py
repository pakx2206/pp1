a = int(input("Enter a: "))
b = int(input("Enter b: "))

for x in range(1, a+1):
    if x==1 or x==a:
        print('*'*b)
    else:
        print('*', end='')
        print(' '*(b-2),end='')
        print('*', end='\n')