from common_math import *
import numpy as np
import random
from scipy.linalg import solve
import copy

def add(a,b,n):
    if len(a)!=len(b):
        return 0
    res=[0 for i in a]
    for i in range(len(a)):
        res[i]=add_mod(a[i],b[i],n)
    return res

def sub(a,b,n):
    if len(a)!=len(b):
        return 0
    res=[0 for i in a]
    for i in range(len(a)):
        res[i]=sub_mod(a[i],b[i],n)
    return res 
def mul(a,b,n):
    if len(a)!=len(b):
        return 0
    res=[0 for i in a]
    for i in range(len(a)):
        res[i]=mul_mod(a[i],b[i],n)
    return res    
def div(a,b,n):
    if len(a)!=len(b):
        return 0
    res=[0 for i in a]
    for i in range(len(a)):
        res[i]=div_mod(a[i],b[i],n)
    return res  
def mul_num(a,b,n):
    res=[0 for i in a]
    for i in range(len(a)):
        res[i]=mul_mod(a[i],b,n)
    return res
def div_num(a,b,n):
    res=[0 for i in a]
    for i in range(len(a)):
        res[i]=div_mod(a[i],b,n)
    return res
    

def get_rank(coef,n):
    c=copy.deepcopy(coef)
    l=len(c)
    if l==1:
        return 1
    for i in range(l):
        k=0
        try:
            while c[i][i]==0:
                t=c[i]
                del c[i]
                c.append(t)
                k+=1
                if k==l-i:
                    raise Exception()                
        except:
            continue
            
        for j in range(i+1,l):
            
            t1=LCM(c[j][i],c[i][i])
            ti=t1//c[i][i]
            tj=t1//c[j][i]
            c[j]=sub(mul_num(c[j],tj,0),mul_num(c[i],ti,0),n)
            
            
    zero=[0 for i in c[0]]
    rk=l
    for i in range(l-1,-1,-1):
        if c[i] == zero:
            rk-=1
        else:        
            return rk
    return 0
            
def solve(coef,cb,n):
    c=copy.deepcopy(coef)
    b=copy.deepcopy(cb)
    l=len(c)
    if l==1:
        return 0
    for i in range(l):
        k=0
        try:
            while c[i][i]==0:
                t=c[i]
                del c[i]
                c.append(t)
                t=b[i]
                del b[i]
                b.append(t)
                k+=1
                if k==l-i:
                    raise Exception()                
        except:
            continue
            
        for j in range(i+1,l):
            #ti=div_mod(c[j][i],c[i][i],n)
            #c[j]=sub(c[j],mul_num(c[i],ti,n),n) 
            #b[j]=sub_mod(b[j],mul_mod(b[i],ti,n),n)
            
            t1=LCM(c[j][i],c[i][i])
            ti=t1//c[i][i]
            tj=t1//c[j][i]
            c[j]=sub(mul_num(c[j],tj,0),mul_num(c[i],ti,0),n)
            b[j]=sub_mod(b[j]*(tj),b[i]*(ti),n)
    for i in range(l-1,-1,-1):
        b[i]=div_mod(b[i],c[i][i],n)
        c[i][i]=1
        for j in range(i):
            b[j]=sub_mod(b[j],mul_mod(b[i],c[j][i],n),n)
            c[j][i]=0
            
    return b

def index_calculus(a,b,n,B):
    prime_list=Gen_prime_less_or_equal_than_n(B)
    coefs=[]
    coef_b=[]
    while True:
        
        kr=random.randint(0,n-1)
    #for kr in [48,100,186,2986]:
        k=pow_mod(a,kr,n)
        k_factor=Eratosthenes_sieve(k)
        coef=[0 for i in range(len(prime_list))]
        try:
            for i in k_factor:
                if i[0] not in prime_list:
                    raise Exception()
                coef[prime_list.index(i[0])]=i[1]
        except:
            continue
        coefs.append(coef)
        rk=get_rank(coefs,n)
        if rk!=len(coefs):
            coefs.pop()
            continue
        coef_b.append(kr)
        if rk == len(prime_list):
            break
    
    x=solve(coefs,coef_b,n-1)
    #x=[1100,2314,366,220]
    #x=[12, 3354, 1198, 700]

    while True:
        kr=random.randint(0,n-1)
        k=mul_mod(b,pow_mod(a,kr,n),n)
        k_factor=Eratosthenes_sieve(k)
        coef=[0 for i in range(len(prime_list))]
        try:
            for i in k_factor:
                if i[0] not in prime_list:
                    raise Exception()
                coef[prime_list.index(i[0])]=i[1]
        except:
            continue
        res=-kr
        for i in range(len(coef)):
            res+=coef[i]*x[i]
        #pay attention here, when we need to simplify res, we need to use Fermat or Euler theory, so, we should module phi(n), not n               
        res%=EulerPhi(Eratosthenes_sieve(n))  
        return res
        
    
    
    
if __name__=='__main__':
    a=22
    b=4
    n=3361
    B=10
    c=[[5,2,0,0],[6,0,0,1],[9,0,1,0],[3,1,2,0]]
    #b=[48,100,186,2986]
    #solve(c,b,n-1)
    print index_calculus(a,b,n,B)
    #coef=[[1,2,3,4],[2,3,4,5],[3,4,5,7]]
    #print get_rank(coef)
    #a=[2,3,4,5,6]
    #b=[3,4,5,6,7]
    #n=0
    #print add(a,b,n)
    #print sub(a,b,n)
    #print mul(a,b,n)
    #print div(a,b,n)
    #print mul_num(a,6,n)
    #print div_num(a,6,n)
    #c=[]
    #for i in range(10):
     #   t=[]
        
      #  for j in range(10):
       #     t.append(random.randint(1,96))
        #c.append(t)
    #print c
    #print get_rank(c,n)
    #print 
    #print 
        