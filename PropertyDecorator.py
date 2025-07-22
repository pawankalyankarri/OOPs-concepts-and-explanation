#  Property decorator is only for getter and setter methods 

#  They will make setter and getter methods behave like methods inside the class but they behave like variabels
# outside the class

class Student:
    def __init__(self,n,a,g):
        self.__name = n
        self.__age = a
        self.__gender = g
        
    def info(self):
        print(self.__name)
    
    @property                       #getting
    def getname(self):
        return self.__name
    
    @getname.setter                 #setting
    def getname(self,n):
        if n.isalpha():
            self.__name = n
            
            
s1 = Student('srija',45,'female')


res = s1.getname
print(res)

