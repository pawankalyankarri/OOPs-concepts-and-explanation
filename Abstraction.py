# Abstration => 
# Hiding the implementation to the outside of the world is abstration

#abstract method => These are empty methods
    # The methods are only having declaration not having definition those methods are called abstract method
    
#abstract class =>
    # The class which are having abstract methods those classes are called abstract class
    
    
from abc import ABC,abstractmethod
class Decide(ABC):
    def __init__(self,num):
        self.num = num
    
    @abstractmethod   
    def isprime(self):
        pass
    
    @abstractmethod
    def isstrong(self):
        pass
    
    
    def info(self):
        print('from Abstract main class ', self.num)
    
    
    
    
        
        

