


class Student:
    def __init__(self,name,age,gender,m1,m2):
        self.name = name
        self.age = age
        self.gender = gender
        self.m1 = m1
        self.m2 = m2
        
    def info(self):
        print(self.name,self.age,self.gender)
        
    def totalmarks(self):
        return (self.m1+self.m2)//2
    
    def getgrade(self):
        tm = self.totalmarks()
        if tm>80:
            return 'A'
        elif tm>60:
            return 'B'
        else:
            return 'C'
        
std = Student('Raju',45,'male',90,80)
grade = std.getgrade()
print(grade)