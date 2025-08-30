class Quantity:
    def __init__(self,q):
        self.q = q

        
        
    def __add__(self,other):
        return self.q+other.q
    
    
    def __mul__(self,other):
        return self.q*other.q
    
    def __truediv__(self,other):
        return self.q/other.q
    
    def __sub__(self,other):
        return self.q-other.q
    
    def __str__(self):
        return str(self.q)
    
    def __repr__(self):
        return str(self.q)

a = Quantity(10)

b = Quantity(100)

print([a,b])