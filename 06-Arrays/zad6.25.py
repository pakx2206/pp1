def occurs(number,array):
    for x in range(0,len(array)):
        if number==array[x]:
            return True
        else:
            return False

print(occurs(23,[15,38,7,23,14]))