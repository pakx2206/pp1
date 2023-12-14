def star(n):
    return f'{n}: {"*"*n}'

arr = [12,6,4,9,10]

for x in range(0,len(arr)):
    print(star(arr[x]))