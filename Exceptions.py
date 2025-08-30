try:
    n1 = int(input('Enter num'))
    n2 = int(input('enter n2'))
    res = n1//n2

except ValueError:
    print('input should be integer')

except ZeroDivisionError:
    print('denominator should not be zero')
    
    
except Exception:
    print('something wrong')
    
else:
    print(res,'success')
    
finally:
    print('this is finally')