def f(password):
    if len(set(password))>=6 and len(password):
        return True
    else:
        return False
    
print(f("ax15"))        # Output: False
print(f("book123"))     # Output: False
print(f("A2water3"))    # Output: True
print(f("qwerty"))      # Output: True
print(f(""))
    
print(set("book123"))