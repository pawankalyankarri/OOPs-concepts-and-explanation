from singleInheritance import Bank

class NewBank(Bank):
    def compoundInterest(self):
        # return (self.p*((1+(self.r)/100)**self.t) -1)
        res = self.p*(((1+(self.r)/100)**self.t)-1)
        return res
    
    
    def info(self):
        print('NewBank from ')
        super().info()