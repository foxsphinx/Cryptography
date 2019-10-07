from common_math import *
import time

def Shanks(n,base,module):
    m=int(math.ceil(math.sqrt(module)))
    table=[]
    for i in range(m):
        table.append((i,cal_power_model(base,i,module)))
    a_with_index_minus_m=pow_mod(base,m,module)
    a_with_index_minus_m=div_mod(1,a_with_index_minus_m,module)
    gamma=n
    for i in range(m-1):
        for j in table:
            if gamma ==j[1]:
                return i*m+j[0]
        gamma=mul_mod(gamma,a_with_index_minus_m,module)
        
    return 0

if __name__=='__main__':
    n=75
    base=13
    module=97
    t1=time.time()
    i = Shanks(n,base,module)
    print i
    t2=time.time()
    
    print t2-t1
    t1=time.time()
    for i in range(n):
        t=pow_mod(base,i,module)
        if t==n:
            print i
    t2=time.time()
    print t2-t1
            
