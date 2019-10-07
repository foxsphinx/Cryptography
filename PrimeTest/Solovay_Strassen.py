import math
import random
from common_math import *
from Legendre import *


def Solovay_Strassen(p,n):
    if p==2:
        return True
    if p%10 in (0,2,4,6,8):
        return False
    for i in range(n):
        ri=random.randint(1,p-1)
        r1=Legendre_symbol(ri,p)
        if r1 <0 :
            r1+=p
        r2=pow_mod(ri,(p-1)//2,p)
        if r1 != r2:
            return False
    return True

if __name__=='__main__':
    for i in range(2,100):
        if Solovay_Strassen(i,50):
            print i
            
        