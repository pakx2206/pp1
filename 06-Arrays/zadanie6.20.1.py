def star(n):
    arr = [12, 6, 4, 9, 10]
    for x in range(0, len(arr)):
        z = int(arr[x])
        print(str(f'{z}: {z*"*"}'))


star(5)
