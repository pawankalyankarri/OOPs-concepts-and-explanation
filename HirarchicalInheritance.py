#hirarchical inheritance => one parent class inherit to two differnt child class

class Animal:
    def display(self):
        print('Animal')
        
class Bird(Animal):
    def show(self):
        print('Bird')
        super().display()
        
class Fish(Animal):
    def show(self):
        print('Fish')
        super().display()
        
        
f = Fish()
b = Bird()

f.show()
