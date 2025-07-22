from singleInheritanceNewBank import NewBank

b = NewBank('aravindh',1000,10,2)
b.info()
res = b.simpleInterest()
print('simpleinterest',res)
res = b.compoundInterest()
print('compoundinterest',res)