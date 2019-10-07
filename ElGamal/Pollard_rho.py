from common_math import *

def f(x,alpha,beta,n):
    t=x%3
    if t==0:
        return (beta*x)%n
    elif t==1:
        return (x*x)%n
    else:
        return (alpha*x)%n
    
def ax(x,a,n):
    t=x%3
    if t==0:
        return a
    elif t==1:
        return (a*2)%n
    else:
        return (a+1)%n    
    
def bx(x,b,n):
    t=x%3
    if t==0:
        return (b+1)%n
    elif t==1:
        return (b*2)%n
    else:
        return  b   
    
def Pollard_rho(alpha,beta,n):
    x0=beta
    a0=1
    b0=1
    table=[(x0,a0,b0)]
    for i in range(1,n):
        x=f(x0,alpha,beta,n)
        a=ax(x0,a0,n)
        b=bx(x0,b0,n)
        x0=x
        a0=a
        b0=b
        table.append((x0,a0,b0))
        if i%2==0:
            x=table[i//2][0]
            a=table[i//2][1]
            b=table[i//2][2]
            if x0==x:
                r=(b0-b)%n
                if r ==0 :
                    return 0
                res = mul_mod(div_mod(1,r,n),(a-a0),n)
                while res < 0:
                    res+=n
                return res
    return 0
    
if __name__=='__main__':
    res=Pollard_rho(2,228,190)
    print res
        