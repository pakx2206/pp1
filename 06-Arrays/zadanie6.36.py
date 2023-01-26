arr = [[2,3,4,5],[1,2,3,4]]
# for x in range(2):
#     for y in range(4):
#         print(arr[x][y], end=" ")
#     print("\r")
for row in arr:
    print(*row)