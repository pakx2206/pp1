a = int(input("Number of products purchased: "))
b = float(input("Product price: "))
sum = 0
for x in range(1,a+1,1):
    if x==1 or x==2:
        sum+=b
    else:
        sum+= b*0.75

print(f'Amount to pay: {sum:.2f}')