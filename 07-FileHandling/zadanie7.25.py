import re
xd = "To be, or not to be, that is the question"
slowa = re.findall(r'\S+',xd)
print(len(slowa))