class Student:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
        
    def info(self):
        print(self.name,self.age)
        
    @classmethod
    def generateObj(cls,st):
        n,a,g = st.split('|')
        obj = cls(n,int(a),g)
        return obj
    
arr = ['siva|35|male','anu|24|female','raj|25|male']
lst = []
for s in arr:
    std = Student.generateObj(s)
    lst.append(std)
    
for l in lst:
    l.info()
    
        
            
        