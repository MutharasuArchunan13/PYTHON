# Inheritance allows us to define a class that inherits all the methods and properties from another class.
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
class advance_calc(calculator):
    def __init__(self,a,b,c=1):
        super().__init__(a,b)
        self.c=c

    def multi(self):
        return self.a * self.a

    def division(self):
        return self.a/self.c

obj = advance_calc(10,20,2)

addition=obj.add()
subtraction =obj.sub()
multi=obj.multi()
div=obj.division()

print(addition,subtraction,multi,div)