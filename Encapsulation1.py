# wrapping up of Data and methods into a single unit is nothing but encapsulation


class Student:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
        
    def info(self):
        print(self.__name,self.__age)
        
        
        
s = Student('siva',25)
s.info()