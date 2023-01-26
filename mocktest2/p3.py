def f(array2D):
    result = []
    for i in range(len(array2D[0])):
        column_sum = 0
        for row in array2D:
            column_sum += row[i]
        result.append(column_sum)
    return result

print(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [12, 15, 18]

    