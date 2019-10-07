from Eratosthenes_sieve import *

def factorial(x,primes):
    res=[]
    for i in primes:
        n=i
        s=0
        while n<=x:
            s+=x//n
            n*=i
        res.append(s)
    return res

def C(n,m):
    primes=Gen_prime_less_or_equal_than_n(n)
    if n<m:
        print 'error'
        return 0
    np=factorial(n,primes)
    mp=factorial(m,primes)
    lp=factorial(n-m,primes)
    for i in range(len(np)):
        np[i]=np[i]-mp[i]-lp[i]
    s=1
    for i in range(len(np)):
        s*=primes[i]**np[i]
    return s

if __name__=='__main__':
    n=1000
    m=3
    a = C(n,m)
    print a
            