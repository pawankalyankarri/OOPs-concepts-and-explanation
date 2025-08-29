class Student:
    inst = 'xyz'
    def __init__(self,n,a,g):
        self.name = n  # these are instance variables
        self.age = a
        self.gender = g
        
    def info(self):
        print(self.name,self.inst)
        
        
std = Student('siva',25,'male')
std.info()