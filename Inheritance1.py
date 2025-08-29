class A:
    def display(self):
        print('this is display from A')
        
    def show(self):
        print('this is show from A')
        

class B(A):
    def show(self):
        super().show()
        print('This is show from B')

b = B()
b.show()
b.display()