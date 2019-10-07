from common_math import *

def Chinese_remain(eqs):
    m=1
    x=0
    for i in eqs:
        m*=i[1]
    for i in eqs:
        M=m//i[1]
        Mp=div_mod(1,M,i[1])
        x+=M*Mp*i[0]
    x%=m
    return x,m


if __name__=='__main__':
    a=[(2,3),(3,5),(2,7)]
    print Chinese_remain(a)