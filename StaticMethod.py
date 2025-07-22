# Static Method  => 
# static method is used to process the individual data. it is not belong to class and not belong to object

class Student:
    """hi how are you"""
    def __init__(self,n,g):
        self.name = n
        self.gender = g 
    
    
        
    def info(self):
        print(self.name,self.gender)
    
    @staticmethod    
    def isyoung(age):
        if age>60:
            return 'old'
        elif age>30:
            return 'Middle'
        elif age>18:
            return 'younger'
        else:
            return 'teen'
        
    
        
        
s = Student('siva','male')

s.info()
res = s.isyoung(25)
print(res)
print(Student.__doc__)  #it is for reading documention about class
    
        