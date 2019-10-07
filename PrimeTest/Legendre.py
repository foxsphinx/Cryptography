import math
from common_math import *
from Eratosthenes_sieve import *

def Legendre_symbol(q,p):
    if q%p == 0:
        return 0
    if q == 1:
        return 1
    if q == -1:
        if p%4 == 1:
            return 1
        if p%4 == 3:
            return -1
    if q ==2:
        if p%8 in (1,7):
            return 1
        if p%8 in (3,5):
            return -1
    if q<p and isSqrtNum(q) :
        return 1
    if q>p :
        return Legendre_symbol(q%p,p)
    
    qt=Eratosthenes_sieve(q)
    pt=Eratosthenes_sieve(p)
    if len(qt) ==1 and len(pt) == 1:
        return Legendre_symbol(p,q)*((-1)**((p-1)*(q-1)//4))
    elif len(qt) !=1 :
        res=1
        for i in qt:
            res*=Legendre_symbol(i[0],p)**i[1]
        return res
    else:
        res=1
        for i in pt:
            res*=Legendre_symbol(q,i[0])**i[1]
        return res
    

if __name__=='__main__':
    print Legendre_symbol(3,10)
                        