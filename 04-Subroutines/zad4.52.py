def pow(x,n):
    if n==1:
        return x
    return x*pow(x,n-1)

print(pow(2,3))