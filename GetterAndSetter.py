class Student:
    def __init__(self,n,a,g):
        self.__name = n
        self.__age = a
        self.__gender = g
    
    def info(self):
        print(self.__name,self.__age,self.__gender)
        
    def getage(self):
        return self.__age
    
    def setage(self,na):
        if na>0 and na<100:
            self.__age = na
        return self.__age
    
    
std = Student('rajesh',45,'male')
res = std.getage()
print(res)
std.setage(100)
std.info()


        
        
        
        
