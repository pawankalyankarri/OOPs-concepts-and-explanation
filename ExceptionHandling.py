# Three type of exception those are
# syntax error
# logical error
# runtime error


try:
    num = int(input('Enter a number'))
    den = int(input('Enter a denominator:'))
    res = num//den
    
except ZeroDivisionError:
    print('denominator should not be zero')   
except ValueError:
    print('sting not allow') 
except Exception:
    print('failed')
else:
    print(res)
finally:
    print('it is finally block')
