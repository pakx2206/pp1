def f(s):
    for x in range(0,16,1):
        if x in range (12,16) or x in range (0,2): print(s[x], end="")
        else: print("*", end="")

f("5290312400019022")