import math

def trial_division(n):
    if n ==2:
        return True
    a=int(math.ceil(math.sqrt(n)))
    for i in range(2,a+1):
        if n%i ==0:
            return False
    return True

if __name__=='__main__':
    for i in range(2,100):
        if trial_division(i):
            print i