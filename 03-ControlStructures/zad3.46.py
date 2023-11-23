for x in range(1,8,1):
    for y in range(0,43,7):
        if 0<y<42:
            print(f'{(x+y):2}',end=' ')
        elif y==0:
            print(x+y, end=' ')
        else:
            print(x+y, end='\n')
        