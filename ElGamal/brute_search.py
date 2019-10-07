from common_math import *

def brute_search(a,b,p):
    i=1
    while i < p :
        if pow_mod(a,i,p) == b:
            return i
        i+=1
    return 0

if __name__ == '__main__':
    p=251
    a=71
    b=210  
    print brute_search(a,b,p)