class Student:
    fee = []
    def __init__(self,n,g,f):
        self.name = n
        self.gender = g
        self.fee.append(f)
    
    def info(self):
        print(self.name,self.gender)
    @classmethod   
    def revenue(cls):
        return sum(cls.fee)
    @staticmethod
    def display(a):
        if a>18:
            return 'younger'
        else:
            return 'teen'
        
            
std = Student('siva','male',15000)           

res = std.display(30)
print(res)
            