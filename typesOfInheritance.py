##single Inheritance

# class A:
#     def __init__(self,n):
#         self.name = n
        
#     def info(self):
#         print(self.name,'from A')
        
        
# class B(A):
#     def show(self):
#         print('This is from B',self.name)
        
        
# b = B('siva')

# b.info()
# b.show()



# # Multilevel Inheritance


# class Human:
#     def __init__(self,n,a,g):
#         self.name = n
#         self.age = a
#         self.gender = g
        
#     def info(self):
#         print(self.name,self.age,self.gender)
        
        
# class Employee(Human):
#     def __init__(self,n,a,g,eid):
#         super().__init__(n,a,g)
#         self.eid = eid
        
#     def info(self):
#         super().info()
#         print(self.eid)
        
# class Manager(Employee):
#     def __init__(self,n,a,g,eid,r):
#         super().__init__(n,a,g,eid)
#         self.rights = r
        
#     def info(self):
#         super().info()
#         print(self.rights)
        
        
# m = Manager('anu',31,'female',543,'special rights')
# m.info()
        

# # Multiple inheritance

# class A:
#     def display(self):
#         print('this is display from A')
        
#     def show(self):
#         print('this is show from A')
        

# class B:
#     def info(self):
#         print('this is info from B')
        
#     def show(self):
#         print('This is show from B')
        
        
        
# class C(A,B):
#     pass


# c = C()

# c.info()
# c.display()
# c.show()
