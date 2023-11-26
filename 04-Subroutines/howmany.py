def howmanyx(text, letter):
    sum = 0
    text = str(text)
    for x in text:
        for y in range(len(x)):
            if x[y]==letter:
                sum+=1
    return sum

