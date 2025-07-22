
#Polymorphism / dynamically typed polymorphism  / runtime polymorphism / Duck Typing

import random
class Dog:
    def sounds(self):
        print('bow bow')
        
class Cat:
    def sounds(self):
        print('meow meow')
        
class Rat:
    def sounds(self):
        print('keech keech')
        
        
d = Dog()
c = Cat()
r = Rat()

arr = [d,c,r]

random.shuffle(arr)

for i in arr:
    i.sounds()