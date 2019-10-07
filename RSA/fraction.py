from common_math import *

class Fraction(object):
    def __init__(self,numerator,denominator):
        comm=GCD(numerator,denominator)
        if numerator*denominator>=0:
            self.numerator=abs(numerator)/comm
            self.denominator=abs(denominator)/comm
        else:
            self.numerator=-abs(numerator)/comm
            self.denominator=abs(denominator)/comm  
            
    def __neg__(self):
        num=-self.numerator
        den=self.denominator
        return Fraction(num,den)
        
    def __add__(self,fra):
        if isinstance(fra, Fraction):
            num=self.numerator*fra.denominator+self.denominator*fra.numerator
            den=self.denominator*fra.denominator
            comm=GCD(num,den)
            num=num/comm
            den=den/comm
            return Fraction(num,den)
        elif isinstance(fra,int):
            return self + Fraction(fra,1)
        else:
            print 'error'
            return
    
    def __sub__(self,fra):
        return self + (-fra)
    
    def __mul__(self,fra):
        if isinstance(fra,Fraction):
            num=self.numerator*fra.numerator
            den=self.denominator*fra.denominator
            comm=GCD(num,den)
            return Fraction(num/comm,den/comm)
        elif isinstance(fra,int):
            return self * Fraction(fra,1)
        else:
            print 'error'
            return        
    
    def __div__(self,fra):
        if isinstance(fra,Fraction):
            num=self.numerator*fra.denominator
            den=self.denominator*fra.numerator
            comm=GCD(num,den)
            if num*den>=0:
                num=abs(num)
                den=abs(den)
            else:
                num=-abs(num)
                den=abs(den)            
            return Fraction(num,den)
        elif isinstance(fra,int):
            return self / Fraction(fra,1)
        else:
            print 'error'
            return    
        
        
    def __pow__(self,n):
        if not isinstance(n,int):
            print 'error'
            return 
        return Fraction(self.numerator**n,self.denominator**n)
    
    
    
    def __str__(self):
        s='%d/%d' %(self.numerator,self.denominator)
        return s
    
    def decimal(self):
        return float(self.numerator)/float(self.denominator)
    
    
    
if __name__=='__main__':
    
    t1=Fraction(-1,2)
    t2=Fraction(1,-3)
    t3=t1+t2
    print t3
    t3=t1-t2
    print t3 
    t3=t1*t2
    print t3 
    t3=t1/t2
    print t3 
    t3=t2+t1
    print t3 
    t3=t2-t1
    print t3 
    t3=t2*t1
    print t3  
    t3=t2/t1
    print t3    
    t3=t1+2
    print t3
    t3=t1**3
    print t3
    
    
    