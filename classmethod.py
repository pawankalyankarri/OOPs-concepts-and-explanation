class Student:
    institute = 'Vcube'
    std_fee = []
    
    def __init__(self,n,a,g,f):
        self.name = n
        self.age = a
        self.gender = g
        self.std_fee.append(f)
        
    def info(self):
        print(self.name,self.age,self.gender)
    
    @classmethod    
    def collection(self):
        return sum(self.std_fee)
    
std1 = Student('siva',24,'male',30000)
std2 = Student('priya',27,'female',35000)
std3 = Student('radhika',29,'female',45000)

res = std1.collection()
print(res)
std1.info()
std2.info()
std3.info()
