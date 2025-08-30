# hiding the implementation to the outside of the world is nothing but Abstraction

from abc import ABC,abstractmethod

class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    @abstractmethod   
    def add(self):
        pass
    
    @abstractmethod
    def sub(self):
        pass
    
    
    
class Calc1(Calculator):
    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y
    
    
    
c = Calc1(20,10)
print(c.add())
print(c.sub())
    