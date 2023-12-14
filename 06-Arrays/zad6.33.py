arr = [1,32,5,382,1,17,4,906]

for x in range(len(arr)*5+1):
    print("-",end="")

print("\n|",end = "")
for x in range(len(arr)):
    if arr[x]<10:
        print(f'   {arr[x]}',end="|")
    elif arr[x]<100:
        print(f'  {arr[x]}',end="|")
    else:
        print(f' {arr[x]}',end="|")  
print("\n",end = "")
for x in range(len(arr)*5+1):
    print("-",end="")

      