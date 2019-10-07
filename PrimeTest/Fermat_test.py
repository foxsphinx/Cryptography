import random
from common_math import *

def Fermat_testing(n,t):
    if not (isinstance(n,int) and isinstance(t,int) and t >0):
        print 'parameter error!'
        return False
    if n in (2,3):
        return True
    for i in range(t):
        a=random.randint(2,n-2)
        r=cal_power_model(a,n-1,n)
        if r != 1:
            return False
    return True

if __name__=='__main__':
    for i in range(2,100):
        if Fermat_testing(i,i-1):
            print i
            
        