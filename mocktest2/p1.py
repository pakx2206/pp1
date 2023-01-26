def f(player1, player2):
    for x in range(0,len(player1)):
        if player1[x] == "T":
            player1[x] = 10
        elif player1[x] == "J":
            player1[x] = 11
        elif player1[x] == "Q":
            player1[x] = 12
        elif player1[x] == "K":
            player1[x] = 13
        elif player1[x] == "A":
            player1[x] = 14 
    for x in range(0,len(player2)):
        if player2[x] == "T":
            player2[x] = 10
        elif player2[x] == "J":
            player2[x] = 11
        elif player2[x] == "Q":
            player2[x] = 12
        elif player2[x] == "K":
            player2[x] = 13
        elif player2[x] == "A":
            player2[x] = 14    

    for x in range(0,len(player1)):
        if player1[x] > player2[x]:
            return True
        else: return False

print(f("AJ972","AQT72") )