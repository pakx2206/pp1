def f(player1,player2):
    
    player1 = list(player1)
    player2 = list(player2)
    
    for x in range(0,len(player1)):
        if player1[x]=="A" or player1[x]=="K" or player1[x]=="Q" or player1[x]=="J" or player1[x]=="T":
            player1[x]=10

    for x in range(0,len(player2)):
        if player2[x]=="A" or player2[x]=="K" or player2[x]=="Q" or player2[x]=="J" or player2[x]=="T":
            player2[x]=10
    sum1 = 0
    sum2 = 0
    for x in range(0,len(player1)):
        sum1 += int(player1[x])
    for x in range(0,len(player2)):
        sum2 += int(player2[x])
    if sum1>sum2:
        return True
    else:
        return False

print(f("AJ972","AQT72") )
print(f("9532","K8") )