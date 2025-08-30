# static method is use to deal with individual data it is not belong to class or not belong to object


class Student:
    def __init__(self,n):
        self.name = n
        
    def info(self):
        print(self.name)
        
    
    def checkage(self,age):
        if age>18:
            print('major')
        else:
            print('minor')
            
s = Student('anu')

s.checkage(50)