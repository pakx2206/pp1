def f(s):
    
    try: 
        s=int(s, base=2)
    except ValueError:
        return False
    return True

print(f("19120"))
print(f("1010101"))
    