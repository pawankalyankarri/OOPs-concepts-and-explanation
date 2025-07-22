class A:
    def display(self):
        print('A')
        
class B(A):             #single inheritance
    def show(self):
        print('B')
        super().display()
        
class C(A):             #Hirarchical
    def show(self):
        print('C')
        super().display()
   
class S:
    def display(sef):
        print('S')
        
        
class D(S,A):  #Multpiple 
    pass

d = D()
d.display()
