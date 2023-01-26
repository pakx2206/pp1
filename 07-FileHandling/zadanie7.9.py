with open('07-FileHandling/numbers.txt', 'r') as f:
    sum = 0
    for line in f:
        number = int(line)
        sum += number

print(sum)
