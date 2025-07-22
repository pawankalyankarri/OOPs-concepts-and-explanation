class A:
    def display(self):
        print('display from the A')
        
    def show(self):
        print('show from the B')
        
        
        
class B(A):
    def display(self):
       print('display from B')
       super().display()
       
    def show(self):
        print('show from B')
        super().show()
        
        
        
a = A()
b = B()

# a.display()
# a.show()
# b.display()
# b.show()



class Student:
    def __init__(self,n,a,g):
        self.__name = n
        self.__age = a
        self.gender = g
    
    def info(self):
        print(self.__name,self.__age,self.gender)
        
        
class Employee(Student):
    def info(self):
        #print(self.__name)  # This is through error
        super().info()
        
emp = Employee('siva',45,'male')
#emp.info()

#passing data to the parent __init__ method 

class Human:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
        
    
class Worker(Human):
    def __init__(self,n,a,g):
        print('Worker class ')
        super().__init__(n,a,g)
        
    def info(self):
        print(self.name,self.age,self.gender)
        
    
w = Worker('hari',45,'Male')
w.info()
        