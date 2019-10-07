from common_math import *

######################################################
# Using Pollard p-1 method to factor.                #
# n: the number to factor                            #
# boundary: the boundary which is needed in this     #
# algorithm. The larger the more possible to factor  #
# but definitely the more time required.             #
######################################################


def p_minus_1_factoring(n,boundary):
    a=2
    for i in range(2,boundary+1):
        a=cal_power_model(a,i,n)
    d=GCD(a-1,n)
    if 1<d and d<n:
        #print "success! d=%s" %d
        return d
    else:
        return 0
    
if __name__=='__main__':
    n=15770708441
    B=180    
    p=p_minus_1_factoring(n,B)
    if p !=0:
        print 'success!'
        print '%d*%d=%d' %(p,n/p,n)
        
        