def f(expression):
    if len(expression)==3:
        if expression[1]=="+":
            return int(expression[0])+int(expression[2])
        else:
            return int(expression[0])-int(expression[2])
    else:
        sum = 0
        if expression[1]=="+":
            sum = int(expression[0])+int(expression[2])
        else:
            sum = int(expression[0])-int(expression[2])
        for x in range(3,len(expression),2):
            if expression[x]=="-":
                sum -= int(expression[x+1])
            else:
                sum += int(expression[x+1])
        return sum
print(f("2+3-4+5-0") )