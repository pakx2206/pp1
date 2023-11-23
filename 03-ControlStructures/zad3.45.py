import math
n = int(input("Enter n: "))

for x in range(2,1000000,1):
    it=0
    for y in range(2,math.isqrt(x)+1):
        if x%y==0:
            it+=1
    if it==0:
        print(x)
        n-=1
    if n==0:
        break

    