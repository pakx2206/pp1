y = str(input("Name: "))
for x in range(0,len(y)):
    print(f'{y[x]}({ord(y[x])})',end=' ')