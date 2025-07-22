class Calc1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b
    def substration(self):
        return self.a-self.b
    
    
class Calc2:
    def __init__(self,c,d):
        self.c = c
        self.d = d
    
    def multiplication(self):
        return self.c*self.d
    
    def division(self):
        if self.c>self.d:
            res = self.c//self.d
        else:
            res = self.d//self.c
        return res
    
    
class Calculator(Calc1,Calc2):
    def __init__(self,p,q):
        Calc1.__init__(self,p,q)
        Calc2.__init__(self,p,q)
        
    
c = Calculator(5,15)
res = c.addition()
print('add',res)
res = c.substration()
print('sub',res)
res = c.multiplication()
print('mul',res)
res = c.division()
print('div',res)