class Employee:
    def __init__(self,n,a,g):
        self.__name = n
        self.age = a
        self.__gender = g
        
    def info(self):
        print(self.__name,self.age,self.__gender)
        
        
emp = Employee('raju',45,'male')
emp.info()
emp.age = 55
emp.info()
emp.__gender = 'female'
emp.info()
emp.__name = 'siva'
emp.info()