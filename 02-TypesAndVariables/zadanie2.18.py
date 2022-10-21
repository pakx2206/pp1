import math
a=int(input("bok a:"))
b=int(input("bok b:"))
c=int(input("bok c:"))
p=(a+b+c)/2
print(round(math.sqrt(p*(p-a)*(p-b)*(p-c))))