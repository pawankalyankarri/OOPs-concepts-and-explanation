class Student:
    def __init__(self,n,a,g):
        self.__name = n
        self.__age = a
        self.__gender = g
        
    def info(self):
        print(self.__name,self.__age,self.__gender)
     
    
    def getage(self):
        print(self.__age)
    
    def setage(self,na):
        if na>5 and na <100:
            self.__age = na
    
    
        
    
    
std = Student('siva',23,'male')
std.age = 26
std.__name = 'raj'
std.setage(45)
std.info()
        