def f(card_number):
    y = ""
    for x in range(len(card_number)):
        if x==0 or x==1 or x==12 or x==13 or x==14 or x==15:
            y+=card_number[x]
        else:
            y+="*"
    return y
