class A:
    def display(self):
        print('This is from A')
        
class B(A):
    def show(self):
        print('This is from B')
        
        
a = A()
b = B()

a.display()
b.display()
b.show()