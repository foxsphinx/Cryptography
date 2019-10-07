import copy
import math

def polynomial_div_intdomain(polynomial1,polynomial2):
    n=copy.copy(polynomial1)
    m=copy.copy(polynomial2)
    div=[]
    while True:
        nl=len(n)
        ml=len(m)
        if (nl < ml):
            return div,n
        t=n[0]//m[0]
        div.append(t)
        for i in range(ml):
            n[i]-=m[i]*t
        n.remove(0)
    
def polynomial_multiply(n,m):
    nl=len(n)
    ml=len(m)
    res=[0 for i in range(nl+ml-1)]
    for i in range(nl):
        for j in range(ml):
            res[i+j]+=m[j]*n[i]
    return res
        
def polynomial_add(n1,m1):
    nl=len(n1)
    ml=len(m1)
    n=copy.copy(n1)
    m=copy.copy(m1)

    if nl>ml:
        for i in range(nl-ml):
            m.insert(0,0)
            ml=nl
    else:
        for i in range(ml-nl):
            n.insert(0,0)
            nl=ml
    res=[]
    for i in range(nl):
        res.append(n[i]+m[i])
            
    while res:
        if res[0] == 0:
            res.remove(0)
        else:
            break
    if res:
        return res
    else:
        return [0]
    

def polynomial_sub(n1,m1):
    nl=len(n1)
    ml=len(m1)
    n=copy.copy(n1)
    m=copy.copy(m1)

    if nl>ml:
        for i in range(nl-ml):
            m.insert(0,0)
            ml=nl
    else:
        for i in range(ml-nl):
            n.insert(0,0)
            nl=ml
    res=[]
    for i in range(nl):
        res.append(n[i]-m[i])
            
    while res:
        if res[0] == 0:
            res.remove(0)
        else:
            break
    if res:
        return res
    else:
        return [0]
    
class Polynomial(object):
    def __init__(self,poly):
        
        if isinstance(poly,list):
            while poly:
                if poly[0] ==0:
                    poly.remove(0)
                else:
                    break
            self.poly=poly
        elif not poly:
            self.poly=[0]            
        elif isinstance(poly, int):
            self.poly=[poly]
        else:
            raise RuntimeError('not support')
    def __add__(self,poly):
        return Polynomial(polynomial_add(self.poly,poly.poly))
    def __sub__(self,poly):
        return Polynomial(polynomial_sub(self.poly,poly.poly))
    def __mul__(self,poly):
        return Polynomial(polynomial_multiply(self.poly,poly.poly))
    def __div__(self,poly):
        d,r=polynomial_div_intdomain(self.poly,poly.poly)
        return Polynomial(d)
    def __mod__(self,poly):
        d,r=polynomial_div_intdomain(self.poly,poly.poly)
        return Polynomial(r)
    def __len__(self):
        return len(self.poly)
    def __str__(self):
        length=len(self.poly)
        if length not in (1,2):
            s='%dx^%d' %(self.poly[0],length-1)
        elif length==2:
            s='%dx' %(self.poly[0])
        else:
            s='%d' %self.poly[0]
            
        for i in range(1,length):
            if self.poly[i] ==0:
                continue
            sign='+' if self.poly[i]>0 else ''
            if length-i-1 not in (1,0):
                s+='%s%dx^%d' %(sign,self.poly[i],length-i-1)
            elif length-i-1:
                s+='%s%dx' %(sign,self.poly[i])
            else:
                s+='%s%d' %(sign,self.poly[i])
        return s
    
        
    
    
if __name__=='__main__':
    a=Polynomial([4,9,0,8,2,2,4])
    b=Polynomial([-4,-9,0,-8,-2,-12,4])
    print b+a
    print b-a
    print a*b
    print a/b
    print a%b
    
    
    
    

        
        