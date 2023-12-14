def median(array):
    if len(array)%2==1:
        return array[int(len(array)/2)]
    else:
        return (array[int(len(array)/2)]+array[int(len(array)/2)-1])/2
    
print(median([1,0,9,3,4,6]))