import math
from Eratosthenes_sieve import *

def isInt(a):
    if isinstance(a,int):
        return True
    elif isinstance(a,float):
        b=int(a)
        if a==b:
            return True
    return False
    
def isSqrtNum(a):
    s=math.sqrt(a)
    return s==int(s)


def extendedGCD(a, b):
    if b == 0:
        return (1, 0, a)
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    while b != 0:
        q = a / b
        r = a % b
        a = b
        b = r
        x = x1 - q*x2
        x1 = x2
        x2 = x
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return(x1, y1, a)

def GCD(a,b):
    (x,y,z)=extendedGCD(a,b)
    return abs(z)

def LCM(a,b):
    return abs(a*b/GCD(a,b))

def get_bin(a):
    b=[]
    while a !=0:
        b.append(a%2)
        a=a/2
    return b

def cal_power_model(base,power,model):
    bin=get_bin(power)
    length=len(bin)
    sum=1
    for i in range(length):
        sum=(sum*sum*(base**bin[length-i-1]))%model
        
    return sum

def EulerPhi(n):
    res=1
    for i in n:
        tmp=int(i[0]**(i[1]-1))
        res*=tmp*(i[0]-1)
    return res

def add_mod(a,b,n):
    return (a+b)%n

def sub_mod(a,b,n):
    return (a-b)%n

def mul_mod(a,b,n):
    return ((a%n)*(b%n))%n

def div_mod(a,b,n):
    g=GCD(b,n)
    if a % g != 0:
        return 0
    bp=b//g
    np=n//g
    x,k,t=extendedGCD(bp,-np)
    x*=t*(a//g)
    while x<0:
        x+=n
    return x%n

def pow_mod(a,b,n):
    return cal_power_model(a,b,n)

def root_mod(a,b,n):
    phi=EulerPhi(Eratosthenes_sieve(n))
    if GCD(a,n) !=1 or GCD(b,phi) !=1:
        return 0
    u,v,t=extendedGCD(b,-phi)
    while u<0:
        u+=phi
    return pow_mod(a,u,n)

if __name__=='__main__':
    a=9
    b=4
    n=33
    #v = div_mod(a,b,n)
    print root_mod(a,b,n) 
    for i in range(1,33):
        print '%d\t%d' %(i,pow_mod(i,4,33))
    