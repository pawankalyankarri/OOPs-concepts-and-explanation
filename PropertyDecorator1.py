class Student:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
     
    
    def info(self):
        print(self.__name,self.__age)
      
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,na):
        if na<100 and na>5:
            self.__age = na
    
            

s = Student('siva',15)
s.age = 10
print(s.age)
s.info()
    
    
    