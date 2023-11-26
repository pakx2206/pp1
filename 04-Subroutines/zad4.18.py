def number(n):
    arr = []
    for x in range(1, n+1):
        arr.append(str(x))
    
    return (' '.join(arr))

print(number(15))