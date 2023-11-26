def f(dice):
    sum = 0
    most = 0
    record = 0
    
    for x in range(1,len(dice)):
        if dice[x-1]==dice[x]:
            sum+=1
            if sum>record:
                most = int(dice[x])
                record = sum

        else:
            sum = 1
    return most

print(f("5233165554211") )
