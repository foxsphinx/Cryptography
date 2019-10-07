from math import *



######################################
# Using Fermat method to factor      #
# n: the number you want to factor   #
# m: the maxima loop turn            #
######################################

def Fermat_factoring(n,m):
    x=int(ceil(sqrt(n)))
    t=2*x+1
    d=x*x-n
    found=False
    for i in range(m):
        if isSqrtNum(d):
            found=True
            break
        d=d+t
        t=t+2
    if not found:
        return 0,0
    x=sqrt(d+n)
    y=sqrt(d)
    return int(x+y),int(x-y)
    
if __name__=='__main__':
    a=1004791
    n=100000  
    x,y=Fermat_factoring(a,n)
    if (x==0 and y==0) or (y==1) or (x==1):
        print "Cannot factor it"
    else:    
        print '%d*%d=%d' %(x,y,x*y)