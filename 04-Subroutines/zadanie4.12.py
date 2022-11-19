def sum(N):
   if N > 1: return N+sum(N-1)
   else: return 1
print(sum(10))
