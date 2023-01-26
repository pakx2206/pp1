filename = input("File name:")
sum = 0
with open(filename,'r') as f:
    for line in f:
        sum+=1
    print("Number of lines:",sum)

