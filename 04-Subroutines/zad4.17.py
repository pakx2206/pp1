def different(n1,n2,n3):
    if n1!=n2!=n3 and n3!=n1:
        return True
    else: 
        return False
    
print(different(1,2,3))