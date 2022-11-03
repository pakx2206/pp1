def f(s,i):
    s=str(s)
    suma=0
    
    if i==True:
        
        for x in range(0,len(s)):
            
            if int(s[x])%2==0:
                
                suma=suma+int(s[x])
    
    if i==False:
        
        for x in range(0,len(s)):
            
            if int(s[x])%2==1:
                
                suma=suma+int(s[x])
    
    return suma

print(f(13115,True))
