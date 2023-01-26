expresion = (input("podaj ekspresso:")).split(" ")
stack = []
for letter in expresion:
    if letter.isnumeric():
        stack.append(int(letter))
    elif letter != "=":
        y = stack.pop()
        x = stack.pop()
        if letter == "+":
            stack.append(x+y)
        elif letter == "-":
            stack.append(x-y)
        elif letter == "/":
            stack.append(x/y)
        elif letter == "*":
            stack.append(x*y)
    elif letter == "=":
        print(stack.pop())
        break
            



