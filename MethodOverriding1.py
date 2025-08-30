class A:
    def display(self):
        print('display from A')
        
    def show(self):
        print('show from A')
        
        
class B(A):
    def show(self):
        # super().show()
        print('from B')
        
b = B()
b.display()
b.show()