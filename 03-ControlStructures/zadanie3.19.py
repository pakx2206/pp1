print("Enter the dog's age in human years:", end=" ")
x=int(input())
suma=21
if x==2: 
    print("The dog's age in dog’s years is 21 years")
if x==1: 
    print("The dog's age in dog’s years is 10.5 years")
if x>2:
    x=x-2
    while x>0:
        suma=suma+4
        x=x-1


print(f"The dog's age in dog’s years is {suma} years")