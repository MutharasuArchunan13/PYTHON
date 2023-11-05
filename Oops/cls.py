#in Oops was linked together based on objects and class is simply known as blueprint and contain attributes(data) and methods(function)

class car:
    def __init__(self,name):
        print('welcome',name)
        self.name=name
    def welcome(self):
        print('helo')
name1 = car('arun')
print(name1.name)

#name2=car.welcome() # TypeError: car.welcome() missing 1 required positional argument: 'self'
''' becaus each mthods have defaultly object reference parameter 'self'  so if you pass the reference'''