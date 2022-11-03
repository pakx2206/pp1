import math
n=int(input("HOW MANY NUMBERS WILL BE SATISFYING FOR YOU?"))
print("PRIME NUMBERS:", end=" ")
y=2
while(n>0):
    f=0
    for x in range(2, math.isqrt(y)+1,1):
        if y%x==0:
            f+=1
            break
    if f==0: 
        print(y, end=" ")
        n-=1
    y+=1
    

