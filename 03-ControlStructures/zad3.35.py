for x in range(1,31,1):
    if x%3==0 and x%5==0:
        print("BINGO", end=' ')
    elif x%3==0:
        print("THREE", end=' ')
    elif x%5==0:
        print("FIVE", end=' ')
    
    else:
        print(x, end=' ')
