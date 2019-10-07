from common_math import *
######################################################
# External function needed by Pollard rho algorithm  #
# the default one is f(x) = x^2 + 1 (mod n)          #
# you can define it by yourself, and it require      #
# two parameters, the first is x, and second is      #
# the number you want to factor, and the return      #
# should be f(x) mod n                               #
# if you don't know what is it, just keep this one   #
######################################################

def default_fun(a,n):
    return (a*a+1)%n


######################################################
# Pollard rho algorithm                              #
# n: number you want to factor                       #
# initial_value: initial value, usually 2            #
# function: external function, the one defined above #
# m: the maxima loop                                 #
######################################################

def rho(n,initial_value,function,m):
    a=initial_value
    b=function(a,n)
    p=GCD(abs(a-b), n)
    i=0
    while p==1 and i<m:
        a=function(a,n)
        b=function(b,n)
        b=function(b,n)
        p=GCD(abs(a-b),n)
        i=i+1
    if p in (1,n):
        return 0
    else:
        return p



if __name__=='__main__':
    n=455459
    initial_value=2
    max_try=10000
    p=rho(n,initial_value,default_fun,max_try)
    if p !=0:
        print 'success!'
        print '%d*%d=%d' %( p, n/p,n)
    