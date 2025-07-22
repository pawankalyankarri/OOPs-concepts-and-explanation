from Abstraction import Decide
from abc import ABC,abstractmethod

class Confirm(Decide):
    def isprime(self):
        for d in range(2,(self.num//2)+1):
            if self.num%d == 0:
                return False
        else:
            return True
        

    def isstrong(self):
        n = self.num
        s = 0
        while n>0:
            s+= n
            n-=1
        return s == self.num
    
    
            
        
        
        
        
class FindNum(ABC):
    def __init__(self,num):
        self.num = num
    @abstractmethod    
    def isprime(self):
        pass
    @abstractmethod
    def isarmstrong(self):
        pass
    @abstractmethod
    def isperfect(self):
        pass
    
    def info(self):
        print('This is from Base class',self.num)
    
    
    
        