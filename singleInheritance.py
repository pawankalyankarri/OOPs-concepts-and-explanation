class Bank:
    def __init__(self,n,p,t,r):
        self.name = n
        self.p = p
        self.t = t
        self.r = r
    
    def info(self):
        print(self.name)
        
    def simpleInterest(self):
        return (self.p*self.t*self.r)/100
    
