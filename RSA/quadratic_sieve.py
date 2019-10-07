from common_math import *
from fraction import *
from Eratosthenes_sieve import *
import math
import numpy as np

def prepare_sieve(n,m):
    res=[]
    sqrtN=int(math.floor(math.sqrt(n)))
    for i in range(1,m+1):
        res.append(i + sqrtN)
    return res
        


def quadratic_sieve_factoring(n,m):
    res=prepare_sieve(n,m)
    vectorized=[]
    prime=[]
    tmp=[]
    for i in res:
        P=i%n
        Q=1
        W=(i*i-Q*n)%n
        w=None
        if W>n/2:
            w=Eratosthenes_sieve(n-W)
            w.insert(0,(-1,1))
        else:
            w=Eratosthenes_sieve(W)
            w.insert(0,(-1,0))
        if w is not None:
            tmp.append((P,w))

    #print tmp
    for i in tmp:
        for j in i[1]:
            if j[0] not in prime:
                prime.append(j[0])
    prime.sort() 
    #print prime

    for i in tmp:
        vec=[0 for k in range(len(prime))]
        for j in i[1]:
            if j[1] >0:
                vec[prime.index(j[0])]=j[1]
        vectorized.append((i[0],np.array(vec)))
    #print vectorized
    vec=[0 for k in range(len(prime))]
    length=len(vectorized)
    i=0
    while True:
        i+=1
        if i >= 2**length:
            break
        sqrtd=np.array(vec)
        k=get_bin(i)
        m=1
        a=[]

        for j in range(len(k)):
            if k[j]==1:
                sqrtd+=vectorized[j][1]
                sqrtd%=2
                a.append(vectorized[j])
                #m*=vectorized[j][0]
        if (sqrtd == vec).all():
            #print a
            p=1
            q=1
            for l in a:
                p=p*l[0]
                for o in range(len(l[1])):
                    if o>0:
                        q*=prime[o]**l[1][o]

            #print p, int(math.sqrt(q))
            q=int(math.sqrt(q))
            if GCD(n,abs(p-q)) not in (n,1):
                return GCD(n,abs(p-q))
            if GCD(n,abs(p+q)) not in (n,1):
                return GCD(n,abs(p+q))                
    return 0
    
    
if __name__=='__main__':
    n=10373
    m=50
    i=quadratic_sieve_factoring(n,m)
    if i !=0:
        print 'success'
        print '%d*%d=%d' %(i,n/i,i*(n/i))
    else:
        print "can't factor it"
    
                
            
        
                       
                    
                
            
        
