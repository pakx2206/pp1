import shutil
org = '07-FileHandling/text.txt'
copy = '07-FileHandling/copylines.txt'
shutil.copy(org,copy)
with open(copy,'r') as f:
    print(f)
    