from common_math import *
from Chinese_remainder import *
from Shanks_Baby_Step_Giant_Step import *
###############################################################################
# this program uses Pohlig Hellman algorithm to find the Discrete Logarithm.  #
# a: base                                                                     #
# b: the value you want to calculate Discrete Logarithm                       #
# p: module and it must be a prime                                            #
###############################################################################
def Pohlig_Hellman(a,b,p):
    '''this algorithm use Shanks' Baby Step Giant Step as the lower Discrete Logarithm algorithm, 
    if you don't want it you can set the one you prefer in lowlevel_algorithm.
    This algorithm use Eratosthenes Sieve to factor the order, if you don't want to use it,
    you can set you perfer in m'''
    
    
    lowlevel_algorithm=Shanks
    n=p-1
    m=Eratosthenes_sieve(n)
    
    
    x=[]
    for i in m:
        q=i[0]
        e=i[1]
        gamma=1
        l=[0 for k in range(e)]
        a_bar=pow_mod(a,n//q,p)
        b_bar=pow_mod(div_mod(b,gamma,p),n/q,p)
        l[0]=lowlevel_algorithm(b_bar,a_bar,p)
        for j in range(1,e):
            gamma=mul_mod(gamma,a**(l[j-1]*(q**(j-1))),p)
            b_bar=pow_mod(div_mod(b,gamma,p),n/(q**(j+1)),p)
            l[j]=lowlevel_algorithm(b_bar,a_bar,p)
        xi=0
        for j in range(e):
            xi+=l[j]*(q**j)
        x.append( (xi,q**e) ) 
    #print x
    return Chinese_remain(x)[0]


if __name__ == '__main__':
    p=250+1
    a=71
    b=210
    
    x = Pohlig_Hellman(a,b,p)
    print x
    