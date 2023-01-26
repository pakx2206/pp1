arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_names = arr[0]
for name in arr:
    if len(name) > len(longest_names):
        longest_names = name

print(longest_names)
