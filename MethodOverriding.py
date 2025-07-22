#changing the behaviour of the method from the patent class in the child class  is called method overriding

class Human:
    def __init__(self,n,a):
        self.name = n
        self.age = a
        
    def info(self):
        print(self.name)
        
    
class Student(Human):
    def info(self):
        print(self.age)
    def fullinfo(self):
        print(self.name,self.age)
        
        
std = Student('raju',45)
std.info()
std.fullinfo()
    