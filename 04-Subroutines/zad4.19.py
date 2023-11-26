def sum_digits(n):
    sum = 0
    
    for x in range( 0, len(str(n)), 1):
        it = int("1" + "0"*(x+1))
        sum+= int(str(n)[x])%it
    return sum


