a = int(input())
b = int(input())
print("*"*b)
for x in range(0, a-2):
    print("*", " "*(b-4), "*")
print("*"*b, end=" ")
