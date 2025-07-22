class Human:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
    
    def info(self):
        print('This is from Human')
        print(self.name,self.age,self.gender)
        
        
class Employee(Human):
    def __init__(self,n,a,g,salary,eid):
        self.salary = salary
        self.empid = eid
        super().__init__(n,a,g)
        
    def info(self):
        print('This is from Employee')
        super().info()
        print(self.empid,self.salary)
        
        
class Manager(Employee):
    def __init__(self,n,a,g,s,eid,rights):
        self.rights = rights
        super().__init__(n,a,g,s,eid)
        
    def info(self):
        print('This is from Manager')
        super().info()
        print(self.rights)
        
        
        
        
mang  = Manager('rahul',45,'male',450000,65,'pink Slips')

#mang.__init__('siva',34,'male',50000,54,'special') # it will modify the existing values

mang.info()