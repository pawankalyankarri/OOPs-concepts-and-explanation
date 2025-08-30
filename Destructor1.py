# if you want to make any action before deleting object then you need to use destructor

class Display:
    def __init__(self):
        print('object is created')
        
        
    def __del__(self):
        print('this will be deleting')
        
        
d = Display()
