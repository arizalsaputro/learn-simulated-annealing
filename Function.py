from random import uniform

class MyFunction:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.f = lambda x,y: (4-2.1 * x**2 + x**4 / 3) * x**2 + x*y + (-4 + 4* y**2) * y**2

    def calculate(self):
        x,y = {uniform(self.x,self.y),uniform(self.x,self.y)}
        return {'x':x,'y':y,'result':self.f(x,y)}
