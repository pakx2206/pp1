def f(name):
    sum = ""
    words = name.split()
    for x in words:
         sum = sum + x[0]
        
    return sum
   
    

print(f("xddd"))