def occurs(number, array):
    for x in range(len(array)):
        if number == array[x]:
            return True


print(occurs(15, [15, 38, 7, 23, 14]))
