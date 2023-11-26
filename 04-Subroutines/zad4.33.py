def f(n):
    s = ""
    if n==0:
        return s
    elif n==1:
        return "*"
    else:
        s="*"
        for x in range(n-1):
            s+="/*"
        return s
    
print(f(4))
print(f(1))