# destructor method is automatically called when the object is deleted

class Student():
    def __init__(self,n,a):
        self.name = n
        self.age = a
        
    def info(self):
        print(self.name,self.age)
        
    def __del__(self):
        print('object is deleted')
        
        
# std = Student('suri',24)
# std.info()
# del std


def createobj():
    std = Student('suri',24)
    std.info()
    
createobj()
    