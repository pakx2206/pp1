def plane(x, y):
    if x>0 and y>0:
        return f'Point P({x},{y}) is in the first quadrant of the coordinate system'
    elif x<0 and y>0:
        return f'Point P({x},{y}) is in the second quadrant of the coordinate system'
    elif x<0 and y<0:
        return f'Point P({x},{y}) is in the third quadrant of the coordinate system'
    elif x>0 and y<0:
        return f'Point P({x},{y}) is in the fourth quadrant of the coordinate system'
    
print(plane(3,4))
print(plane(-3,4))
print(plane(3,-4))
print(plane(-3,-4))