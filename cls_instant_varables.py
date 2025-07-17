class Student:
    institute = 'Vcube'
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
    
    def info(self):
        print(self.name,self.age,self.gender,self.institute)
        
    
std = Student('raju',32,'male')
std.info()