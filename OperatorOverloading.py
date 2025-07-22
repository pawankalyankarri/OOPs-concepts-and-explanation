#  adding some extra behaviour to the existing operator is called operator overloading

class Quantity:
    def __init__(self,q):
        self.qty = q
    def display(self):
        print(self.qty)
    
    
    def __add__ (self,other):
        return self.qty+other.qty
        
    def __sub__(self,other):
        return self.qty-other.qty
    
    def __mul__(self,other):
        return self.qty*other.qty
    
    def __truediv__(self,other):
        return self.qty/other.qty
    
    def __mod__(self,other):
        return self.qty%other.qty
    
    def __gt__(self,other):
        return self.qty>other.qty
    
    def __lt__(self,other):
        return self.qty<other.qty
    
    def __ge__(self,other):
        return self.qty>=other.qty
    
    def __le__(self,other):
        return self.qty<=other.qty
    def __eq__(self,other):
        return self.qty == other.qty
    
    
  
        
q1 = Quantity(15)
q2 = Quantity(5)
res = q1>=q2   # try these all + = - * % / < > <= >=
# print(res)


class Student:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
        
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age and self.gender == other.gender
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
s1 = Student('ravi',45,'male')
s2 = Student('rani',35,'female')
print(s1 == s2)

print(s1)
arr = [s1,s2]
print(arr)



#__str__  => when you called individual then only called
            # it is used to print single object

# __repr__ => it is used to print list of objects
