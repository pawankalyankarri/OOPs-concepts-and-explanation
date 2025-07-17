class Student:
    institute = 'vcube'
    std_fee = []
    def __init__(self,n,a,g,m1,m2,f):
        self.name = n
        self.age = a
        self.gender = g
        self.m1 = m1
        self.m2 = m2
        self.std_fee.append(f)
        
    def info(self):
        print(self.name,self.age,self.gender,self.m1,self.m2,self.institute)
        
    def totalmarks(self):
        return (self.m1+self.m2)//2
    
    def getgrade(self):
        tm = self.totalmarks()
        if tm>80:
            grade = 'A'
        elif tm>60:
            grade = 'B'
        else:
            grade = 'C'
            
        return grade
    @classmethod
    def revenue(self):
        return sum(self.std_fee)
    
    @classmethod
    def generateObj(self,st):
        n,a,g,m1,m2,f = st.split('|')
        std= Student(n,int(a),g,int(m1),int(m2),int(f))
        return std
    
arr = ['raju|34|male|99|69|30000',
       'suri|24|female|89|79|20000',
       'arjun|30|male|59|60|25000',
       'praveen|44|female|79|55|30000',
       ]

stds_list = []
for i in arr:
    s = Student.generateObj(i)
    stds_list.append(s)
    
for i in stds_list:
    i.info()
    

        