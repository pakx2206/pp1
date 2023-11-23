a = int(input("Enter number of task: "))
b = int(input("Enter number of taks completed correctly: "))

if float(b/a)>=0.5:
    print("Test passed")
else:
    print("Test failed")