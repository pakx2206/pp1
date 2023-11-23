sum = 0
it = 0
y=1
while y!=0:
    x = int(input("Enter number: "))
    if x==0:
        y=0
    else:
        sum+=x
        it+=1
    
print(f'RESULT: Quantity={it}, Sum={sum}, Mean={int(sum/it)}')