#in multiple inheritance if you are inheriting some properies in differnt way same property is comminng into child class
#by using child class object if you call the property then there is ambligity like which property like class 1 or class2 this
# confusion is diamond problem

class A:
    def __init__(self):
        print('__init__ from A')
        
    def display(self):
        print('display from A')
        
        
class B:
    def __init__(self):
        print('__init__ from B')
        
    def display(self):
        print('display from B')
        
        
class C(B,A):
    def show(self):
        print('show from C')
        
c = C()
c.show()
c.display()# here ambiglity created in which property we need to call based on MRO it calles repective one


#Method Resolution Order(MRO)
#it is following one algorithm called C3Linearization. 
# it identifies which one first inherited to class.
#Mro is solution for diamond problem
        