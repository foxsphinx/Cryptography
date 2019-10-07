import math

def Eratosthenes_sieve(n):
    res=[]
    count=0
    if n<0:
        n=-n
        res.append((-1,1))
    while n%2 == 0:
        n/=2
        count+=1
    if count !=0:
        res.append((2,count))
        count=0
    for i in range(3,n+1,2):
        while n%i == 0:
            n/=i
            count+=1
        if count != 0:
            res.append((i,count))
            count=0
    return res

def Eratosthenes_sieve_mod2(n):
    tmp=Eratosthenes_sieve(n)
    res=[]
    for i in tmp:
        res.append((i[0],i[1]%2))
    return res

def Gen_prime_less_or_equal_than_n(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2,3]
    res=[2]
    table=[x for x in range(3,n+1,2)]
    for i in range(len(table)):
        if table[i] != 0:
            t=2*i+3
            for j in range(2,n//t+1):
                tmp=j*t
                if tmp%2 == 1:
                    table[(tmp-3)//2]=0
    for i in table:
        if i !=0:
            res.append(i)
    return res
    

if __name__=='__main__':
    #n=49
    #print Eratosthenes_sieve(n)
    #print Eratosthenes_sieve_mod2(n)
    Gen_prime_less_or_equal_than_n(97)