import math

q=0
s=0
m=0
while True:
    x=int(input("Enter number:"))
    if x==0: break
    q+=1
    s=s+x
    m=s/q
    

print(f"RESULT: QUANTITY = {q}, SUM = {s}, MEAN = {m}")