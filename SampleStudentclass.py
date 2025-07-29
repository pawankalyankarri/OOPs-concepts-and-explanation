class Student:
    institute = 'Vcube'
    fee = []
    def __init__(self,n,a,m,f):
        self.name = n
        self.age = a
        self.marks = m
        self.fee.append(f)
        
    def info(self):
        print(self.name,self.age,self.marks,self.institute)
    
    @classmethod  
    def revenue(cls):
        return sum(cls.fee)
    
    @classmethod
    def generateobj(cls,s):
        n,a,m,f = s.split(',')
        obj = cls(n,int(a),int(m),int(f))
        return obj

arr = []

str = ['raju,43,70,5000','suri,24,60,40000','hari,20,50,60000']

for i in str:
    obj = Student.generateobj(i)
    arr.append(obj)
    
for i in arr:
    i.info()
        
    
    
