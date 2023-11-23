def coins(x):
    five = 0
    two = 0
    one = 0
    five = int(x/5)
    x = x - 5*five
    two = int(x/2)
    x = x- 2* two
    one = x
    return f'5zł - {five}\n2zł - {two}\n1zł - {one}'

print(coins(18))