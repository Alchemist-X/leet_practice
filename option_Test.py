from functools import cache
@cache
def recursion(r,b):
    if r==0: return 0
    if b==0: return r
    return max(0,r/(r+b)*(1+recursion(r-1,b))+b/(r+b)*(-1+recursion(r,b-1)))

print(recursion(27,27))