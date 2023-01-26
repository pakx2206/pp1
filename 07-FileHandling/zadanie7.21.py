with open('07-FileHandling/power.txt','a') as pow:
    for x in range(1,11):
        pow.write(f'{x},')
        pow.write(f'{x*x},')
        pow.write(f'{x*x*x}')
        pow.write("\n")