class calsi:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2
    def mod(n1,n2):
        return n1%n2
    
    
    
class math:
    def power(a,b):
        return a**b
    def IsEven(val):
        if val%2==0:
            return True
        else:
            return False
    def IsOdd(val):
        if val%2!=0:
            return True
        else:
            return False
        
        
               
class cal:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def __add__(self):
        return self.v1+self.v2
    def __mul__(self):
        return self.v1*self.v2