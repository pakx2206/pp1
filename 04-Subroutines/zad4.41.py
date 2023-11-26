def f(n):
    def isprime(potenital_number):

        for x in range(2,int(potenital_number**0.5)+1,1):
            if potenital_number%x==0:
                return False
        return True
    it=2
    for x in range(1, n+1):
        
        for y in range(it,100000):
            
            if isprime(y)==True and x==n:
                it = y+1
                return y
            elif isprime(y)==True:
                it = y+1
                break
            
print(f(1))
print(f(5))
                