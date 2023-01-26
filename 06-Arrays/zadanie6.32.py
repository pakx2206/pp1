def array_to_string(arr):
    return ",".join(map(str, arr))
my_list = [5,4,3,2,6,5]
print("Array: " + str(my_list))
print("String: " + array_to_string(my_list))

