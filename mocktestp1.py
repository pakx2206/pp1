def f(s):
    a = list(s)
    for x in range(0,16,1):
        if x in range (12,16) or x in range (0,2): continue
        else: a[x] = "*"
        
    b = ' '.join(a)

    
    return b.replace(" ","")
        

print(f("5290312400019022"))