a = str(input("Are you intrested in computer since? (Y/N): "))
if a == "Y":
    a = True
else:
    a = False
b = str(input("Do you like playing computer games? (Y/N): "))
if b == "Y":
    b = True
else:
    b = False
c = str(input("Do you have an Instaagram account? (Y/N): "))
if c == "Y":
    c = True
else:
    c = False
arr = [a,b,c]
for x in range(0,3,1):
    if arr[x]==True:
        arr[x]="Yes"
    else:
        arr[x]="No"

print(f'Interested in computer science: {arr[0]}')
print(f'Playing computer games: {arr[1]}')
print(f'Has an Instagram account: {arr[2]}')
