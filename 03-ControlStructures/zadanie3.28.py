g=50
x=0
y=1
c=0
print(x,y, end=" ")
while(g>0):
    print(x+y, end=" ")
    c=y
    y=y+x
    x=c
    g-=1
    
    
    