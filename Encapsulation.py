# Encapsulation => 
# wrapping up of data and methods into a single unit is called Encapsulation
# Data should not be accessble from the outside and data should be in private mode


class Student:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a 
        
    def info(self):
        print(self.__name,self.__age)
        
        
s1 = Student('sofia',22)
s1.info()