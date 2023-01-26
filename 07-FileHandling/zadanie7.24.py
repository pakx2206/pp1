import re
xd = "To be, or not to be, that is the question"
sum = re.findall('[aeiouyAEIOUY]', xd)
print(len(sum))
