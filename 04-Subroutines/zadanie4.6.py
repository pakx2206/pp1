def dnumbers():
    x = 1
    while x < 10:
        if x % 3 == 0:
            print(x, " ")
        else:
            print(x, end=" ")
        x += 1


print(dnumbers())
