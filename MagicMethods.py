#Magic Methods/special Methods / dhandar methods

# These are special methods they automatically called when action happend.they are starts with the __ and ends
# with __ 

a = 5
b = 10
res = a.__add__(b)
# print(res)
res = a.__sub__(b)
# print(res)
res = a.__mul__(b)
# print(res)
res = b.__truediv__(a)
# print(res)
res = [1,2,3,4,5].__iter__()
it = iter(res)
# print(next(it))
res = [1,2,3,4].__getitem__(0)
# print(res)
a = [1,2,3,4]
res = a.__delitem__(2)
# print(a)

#bottom up approach

#first of all you need to understand one thing what is the most reusable code from that you need to start your code


