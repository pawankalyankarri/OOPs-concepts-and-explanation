class A:
    def display(self):
        print('This is display from A')
        
class B:
    def display(self):
        print('This is display from B')
        

class C(A,B):
    def show(self):
        print('This is show from C')
        
c = C()
c.show()
c.display()