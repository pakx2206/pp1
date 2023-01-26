number = int(input("Natural number:"))
stack = []
while number>0:
    stack.append(number%2)
    number//=2

x = len(stack)
while x>0:
    print(stack.pop())
    x-=1


