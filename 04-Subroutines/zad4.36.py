def f(detector):
    sum = 0 
    for x in range(len(detector)):
        if detector[x]=="+":
            sum+=1
        else:
            if sum>0:
                sum-=1
        if sum==3:
            return True
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))