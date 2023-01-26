import re
import math 
with open('07-FileHandling/grades.txt', 'r') as f:
    xd = f.read()
    sum = re.findall(r'\S+\d', xd)
    wyn = 0
    for x in sum:
        wyn += float(x)
    print(round((wyn/len(sum)),3))
