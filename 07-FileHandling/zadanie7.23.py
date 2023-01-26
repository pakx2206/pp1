import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
temp = temperatures
sum = 0
for x in range(len(temp)):
    sum+=int(temp[x])

print(sum/(len(temp)))
