def f(n):
    stack = []
    if n<=0:
        return (f'""')
    else:
        for x in range(1,n+1):
            stack.append("/")
            if x%5==0 and x!=n:
                stack.append("-")
                
        y = ''.join(stack)
        return (f'"{y}"')

print(f(10)) 
print(f(11))
print(f(-4)) 
print(f(0))
print(f(7))
print(f(5))