import math 
import random
from common_math import *

def Miller_Rabin_test(n,t):
    if n in (2,3):
        return True
    if n%10 in (0,2,4,6,8):
        return False
    s=0
    r=n
    while r%2 !=1:
        r=r//2
        s+=1
    
    for i in range(t):
        a=random.randint(2,n-2)
        y=pow_mod(a,r,n)
        if y not in (1,n-1):
            j=1
            while j <= s-1 and y != n-1:
                y=(y*y)%n
                if y==1:
                    return False
                j+=1
            if y != n-1:
                return False
    return True


if __name__ == '__main__':
    for i in range(2,100):
        if Miller_Rabin_test(i,50):
            print i
            
        