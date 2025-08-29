class Student:
    fee = []
    def __init__(self,n,a,g,f):
        self.name = n
        self.age = a
        self.gender = g
        self.fee.append(f)
        
        
    def info(self):
        print(self.name,self.age,self.gender)
    
    @classmethod    
    def revenue(cls):
        print(sum(cls.fee))
    
    
std = Student('siva',25,'male',30000)
std.info()
std.revenue()