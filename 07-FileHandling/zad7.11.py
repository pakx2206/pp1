f = open("numbers.txt","r")
sum = 0
for numb in f:
    sum+=int(numb)

print(sum)
f.close