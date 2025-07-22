from AbstractImplementation import Confirm
from AbstractImplementation import FindNum

c = Confirm(7)
res = c.isprime()
# print(res)
res = c.isstrong()
# print(res)


class Num(FindNum):
    def isarmstrong(self):
        return self.num == sum([ int(i)**len(str(self.num)) for i in str(self.num)])
    
    def isperfect(self):
        s = 0
        for d in range(1,(self.num//2)+1):
            if self.num % d == 0:
                s+=d
                
        return s == self.num
    
    def isprime(self):
        for d in range(1,(self.num//2)+1):
            if self.num%d == 0:
                return False
        else:
            return True



n = Num(6)
res = n.isarmstrong()
# print(res)
res = n.isperfect()
# print(res)
res = n.isprime()
# print(res)