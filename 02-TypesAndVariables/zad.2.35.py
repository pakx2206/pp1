import math
def cut_the_tree(circumference):
    r = circumference/(2*3.14)
    d = 2*r
    return (d>=50)

print(cut_the_tree(25))