import random
with open('07-FileHandling/numb.txt', 'w')as f:
    for x in range(50):
        a = str(random.randrange(100, 999))
        f.write(a)
        f.write("\n")

        
